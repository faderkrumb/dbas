You can have checks or constraints 
based on attributes (columns) or tuples (rows).

If a constraint includes multiple columns it will be tuple-based.

Functionality: If you have a constraint that includes multiple columns
it will be tuple-based.

a. PostID should be a non-negative integer
b. StartDate should always be on the same day or earlier than EndDate.
c. All tags should be “crypto”, “studying”, “question” or “social”

*Note: You should be able to motivate for 3.a-3.c why the constraints are implemented as
attribute-based or tuple-based.*

a. PostID is attribute-based as it only uses one column and uses SERIAL 
which is an incrementing pseudotype which is never negative.

b. We have flipped this one. ~~endDate is tuple-based as we check 
endDate >= startDate which uses multiple columns.~~
If we would want to flip it back, we would have to put startDate below endDate and put
startDate TIMESTAMP NOT NULL CHECK (startDate \<= endDate).
This is attribute based as both endDate and startDate are in the same column.

c. tags All are attribute-based as we only use one single column to test the constraints.

## Further, database integrity can be maintained by triggers. During the presentation, you should
be able to answer the following:

## 1. What is a trigger?

Triggers is a statement that a system executes automatically when any modification
is made to the database. In a trigger, we first specify when the trigger is to be 
executed, and then the action to be performed when the trigger executes.

## 2. Name 3 events that can cause a trigger to activate

INSERT, UPDATE & DELETE.


## 3. What can be done with triggers?

With triggers we can manipulate data, define data (such as controlling schema
changes, and enforcing security policies, or control/monitor user sessions
or log activity).

