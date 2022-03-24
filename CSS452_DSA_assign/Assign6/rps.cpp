#include <iostream>
using namespace std;

class Tool
{
protected:
  int strength;
  char type;

public:
  void setStrength(int s) { strength = s; }
  bool fight(Tool t);
};

bool Tool::fight(Tool t) {
  if ((type == 'r' && t.type == 'p') || (type == 'p' && t.type == 's') || (type == 's' && t.type == 'r')) {
    if (strength / 2 > t.strength) {
        return true;
    } else {
      return false;
    }
  } else if ((type == 'r' && t.type == 's') || (type == 's' && t.type == 'p') ||
             (type == 'p' && t.type == 'r')) {
    if (strength * 2 > t.strength) {
      return true;
    } else {
      return false;
    }
  }

  if (strength > t.strength) {
    return true;
  } else {
    return false;
  }
};

/*Implement class Scissors */
class Scissors : public Tool {
public:
  Scissors(int s) {
    Tool::setStrength(s);
    type = 's';
  }
};

/*Implement class Paper */
class Paper : public Tool {
public:
  Paper(int s) {
    Tool::setStrength(s);
    type = 'p';
  }
};

/*Implement class Rock */
class Rock : public Tool {
public:
  Rock(int s) {
    Tool::setStrength(s);
    type = 'r';
  }
};

int main() {

                // Example main function

                // You may add your own testing code if you like

                Scissors s1(5);

                Paper p1(7);

                Rock r1(15);

                cout << s1.fight(p1) << p1.fight(s1) << endl;

                cout << p1.fight(r1) << r1.fight(p1) << endl;

                cout << r1.fight(s1) << s1.fight(r1) << endl;

                return 0;

}