
# Concepts and Terms


Before you start implementation, lets get familiar with the terminology that
is used and some basic concepts in ERPNext.




---


### Basic Concepts


#### Company


This represents the Company records for which ERPNext is setup. With this same
setup, you can create multiple Company records, each representing a different
legal entity. The accounting for each Company will be different, but they will
share the Customer, Supplier and Item records.



> 
> Setup > Company
> 
> 
> 


#### Customer


Represents a customer. A Customer can be an individual or an organization.
You can create multiple Contacts and Addresses for each Customer.



> 
> Selling > Customer
> 
> 
> 


#### Supplier


Represents a supplier of goods or services. Your telephone company is a
Supplier, so is your raw materials Supplier. Again, a Supplier can be an
individual or an organization and has multiple Contacts and Addresses.



> 
> Buying > Supplier
> 
> 
> 


#### Item


A Product, sub-product or Service that is either bought, sold or manufactured
and is uniquely identified.



> 
> Stock > Item
> 
> 
> 


#### Account


An Account is a heading under which financial and business transactions are
carried on. Examples of accounts are "Debtors", "Creditors", "VAT Payable", “Travel Expenses”, "Sales", "Share Capital", etc. ERPNext keeps track of your customers' and
suppliers' balances in the background, so you don't need to create dedicated Accounts for them.



> 
> Accounting > Chart of Accounts
> 
> 
> 


#### Address


An address represents location details of a Customer or Supplier. These can be
of different locations such as Head Office, Factory, Warehouse, Shop etc.



> 
> Selling > Address
> 
> 
> 


#### Contact


An individual Contact belongs to a Customer or Supplier or is just an
independent. A Contact has a name and contact details like email and phone
number.



> 
> Selling > Contact
> 
> 
> 


#### Communication


A list of all Communication with a Contact or Lead. All emails sent from the
system are added to the Communication table.



> 
> Support > Communication
> 
> 
> 


#### Price List


A Price List is a place where different rate plans can be stored. It’s a name
you give to a set of Item Prices stored under a particular List.



> 
> Selling > Price List
> 
> 
> 



> 
> Buying > Price List
> 
> 
> 




---

