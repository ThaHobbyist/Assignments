/* Maybe read this from a file? Or some way to pass it from $ py2cfg --port=8001
to the browser? */
let PORT = 8001;

let ws = new WebSocket(`ws://localhost:${PORT}`);
ws.onopen = () => {
    console.log("Websocket connected.")
    ws.send(JSON.stringify({
        "type": "client"
    }))
}

ws.onclose = () => 
{
    console.log("Websocket closed. Closing window")
    window.close()
}
ws.onerror = (event) => console.error(`Websocket error ${event}`);
ws.onmessage = (event) =>
{
    let data = JSON.parse(event.data);
    if (data.type === "log") {
        /* Sanity checks */
        handle_log(data);
    }
    else if (data.type === "cfg") {
        handle_cfg(data);
    }
    else if (data.type === "key") {
        handle_key(data);
    }
    else if (data.type === undefined) {
        handle_undefined(data);
    }
}

function
handle_log(obj)
{
    let message = obj.data
    switch (obj.levelname) {
        case "DEBUG":
            console.trace(message);
            break;
        case "INFO":
            console.debug(message);
            break;
        case "WARNING":
            console.info(message);
            break;
        case "CRITICAL":
            console.warn(message);
            break;
        case "ERROR":
            console.error(message);
            break;
    }
}

function
handle_cfg(obj)
{
    let filepath, layer;
    filepath = obj.filepath;
    layer = obj.layer;
    let cfg, img;
    cfg = document.getElementById("cfg");
    while (cfg.firstChild) {
        cfg.removeChild(cfg.firstChild)
    }
    img = document.createElement("img");
    img.setAttribute("src", filepath);
    img.setAttribute("style", `{z-index:${layer}};`);
    cfg.appendChild(img);
}

function
handle_key(obj)
{
    console.log("Create key element");
    let key, img;
    key = document.getElementById("key");
    img = document.createElement("img");
    img.src = obj.filepath;
    key.appendChild(img);
}