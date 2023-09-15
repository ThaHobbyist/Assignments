/**
 * Project Untitled
 */


#ifndef _TRANSACTIONS_H
#define _TRANSACTIONS_H

class Transactions {
public: 
    void Transaction ID;
    void Book;
    void User;
    void Date_Borrowed;
    void Due_Date;
    void Date_Returned;
    
/**
 * @param user
 * @param book
 * @param ID
 */
void getRecord(void user, void book, void ID);
    
void getTransactions();
    
/**
 * @param ID
 */
void calcPenalty(void ID);
};

#endif //_TRANSACTIONS_H