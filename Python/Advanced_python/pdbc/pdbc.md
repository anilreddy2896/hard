## constraints
  primary key: it should be not null and it should be unique
  not null:will not accept empty input
  unique: it shouldnot have same values across the table it will accepts null values also
  check: to check condition
  default: to set the default value
  foriegnkey: is the key which is primary key in the parent table 

### ddl : data defination language
we cannot rollback or undo the things because it will directly interact with the database and no need of explicitly commiting 
it defines the structure of database(tables)
  1. CREATE TABLE <tablename>
  2. SET UNUSED  <coloumn name> ( will hide instead of deleting)
  3. TRUNCATE TABLE <TABLE NAME> (WILL DELETE DATA BUT NOT STRUCTURE)
  4. RENAME <OLD_NAME> TO <NEW_NAME>
     4.1 ALTER TABLE <TABLE_NAME> RENAME <COLUMN> <OLD_CNAME> <NEW_CNAME>
     4.2 ALTER TABLE <TABLE NAME> RENAME <CONSTRAIN> <OLD_CNAME> <NEW_CNAME>
  5. DROP <TABLE> <TABLE_NAME>
     5.1 ALTER TABLE <TABLE_NAME> DROP <COLUMN>  <CNAME>
     5.2 ALTER TABLE <TABLE_NAME> DROP (<CNAME_0>,<CNAME_1>,<CNAME_2>)
  6. FLASHBACK <TABLE> <TABLENAME>
  7. PURGE
  8. ALTER: 
      8.1 ALTER TABLE <TABLE_NAME> ADD <COLUMN_NAME> <DATA_TYPE><SIZE>
      8.2 ALTER TABLE <TABLE_NAME> MODIFY <COLUMN_NAME> <DATA_TYPE><SIZE>
      8.3 ALTER TABLE <TABLE_NAME> DROP <COLUMN_NAME> 

### DML: DATA MANPULATION LANGUAGE:
    1. SELECT --> IS TO READ THE ENTRIES
       1.1 SELECT * FROM <TABLE NAME>
       1.2 SELECT C1,C2,C3 FROM <TABLE NAME>
       1.3 SELCET * FROM <TABLE_NAME> WHERE C1=<VALUE>
    2. INSERT ---> IS USED TO WRITE
       2.1 INSERT INTO <TABLENAME>(C3,C2,C1) VALUES <V1,V2,V3> 
       2.2 INSERT INTO <TABLENAME> VALUES<V1,V2,V3> 
       2.3 Insert into tablename2 select * from  tablename1   
    3. UPDATE 
       3.1 UPDATE <TABLE_NAME> SET COLUMN_NAME=V1 WHERE COLUMN_NAME=V 
    4.DELETE
       4.1 DELETE <TABLE_NAME>
    5. MERGE 
## TCL: TRANSACTIONAL CONTROL LANGUAGE
    1. COMMIT
    2. ROLLBACK
    3. SAVEPOINT

## DCL : DATA CONTROL LANGUAGUE
    1. GRANT
    2. REVOKE
    3. SETROLE

## clauses :
   to specify certain conditions 
    1> where
    2> like
    3> order by
    4> group by
    5> having
### operators:
  it is used to filter records based on one or more conditions 
  clauses can be combined with the operators 
  1. AND
  2. OR
  3. NOT
  4. between

### joins:
  joins are used to combine two or more tables based on related column
    1. inner join
    2. left join
    3. right join
    4. self join


   
