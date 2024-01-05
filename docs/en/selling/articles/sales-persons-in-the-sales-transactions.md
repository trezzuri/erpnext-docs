
# Sales Persons in the Sales Transactions



In ERPNext, Sales Person master is maintained in [tree structure](/docs/en/setting-up/articles/managing-tree-structure-masters.html). Sales Person is selectable in all the sales transactions.


Sales Persons can be updated in the Customer master as well. On selection of Customer in the transactions, Sales Persons as updated in the Customer will fetch into sales transaction.


![Sales Person Customer](/files/sales-person-in-customer.png)


#### Sales Person Contribution


If more than one sales persons are working together on an order, then contribution (%) should be set for each Sales Person.


![Sales Person Order](/files/sales-person-in-sales-order.png)


On saving transaction, based on the Net Total and Contriution (%), `Contribution to Net Total` will be calculated for each Sales Person.


Total % Contribution for all Sales Person must be 100%. If only one Sales Person is selected, then % Contribution will be 100.
#### Sales Person Transaction Report


Check Sales Person's Transaction report from:


`Selling &gt; Standard Reports &gt; Sales Person-wise Transaction Summary`


This report can be generated based on Sales Order, Delivery Note and Sales Invoice. It will give you total amount of sale made by an employe.


![Sales Person Report](/files/sales-person-wise-transaction-summary-report.png)


#### Sales Person wise Commission


ERPNext only provide total amount of sale made by a Sales Person. If you offer commission to Sales Person, you should add Sales Person as Sales Partners in ERPNext. For Sales Partners, you can define Commission (%). On selected on Sales Partner in a sales transction, based on Net Total, Commission Amount is calculated as well. You can check Sales Partner's commission report from:


`Accounts &gt; Standard Reports &gt; Sales Partners Commission`





