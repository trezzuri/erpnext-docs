
# Upload Backups to Amazon S3



  



> Note: If you are Frappe Cloud user, onsite and offsite backups are automatically created for you: <https://frappecloud.com/docs/sites/backups>
> 
> 

## Prerequisites

* [Email Account](/docs/en/setting-up/email/email-account)

To receive emails for failed and successful backups, please create an **Email Account** first.

## Create S3 bucket and set up access

1. Create a new s3 bucket.

In the bucket settings, enable "Block all public access" to keep your data private. Feel free to enable encryption, versioning or object lock as per your requirements (please refer to [Amazon's documentation](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html)).
2. Open Identity and Access Management (IAM).
3. Create a new policy for the Service "S3", allowing the Actions "ListBucket" and "PutObject".

![Screenshot of "Create Policy" in AWS](/files/s3-backup-policy.png)  


Or, using the JSON editor:


```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::\*/\*",
                "arn:aws:s3:::YOUR TARGET BUCKET"
            ],
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": "YOUR SERVER IP"
                }
            }
        }
    ]
}
  

```
4. Create a new user for programmatic access.

![Screenshot of "Add User" in AWS](/files/s3_backup_add_user.png)
5. Attach the policy you created to the new user.
6. Copy the user's access key and secret.

To automatically delete old backups or move them to a cheaper storage class, have a look at [lifecycle management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html).

## Set up ERPNext

* Open **S3 Backup Settings**.
* Check "Enable Automatic Backup".
* Paste the access key and secret from AWS.
* Set an email address to receive a notification when a backup fails. If you would like an email for successful backups as well, enable "Send Email for Successful Backup".
* Specify the name of the bucket that you created in step 1.
* Choose how often you want to take and upload backups. This can range from monthly to daily. If you only want to take manual backups, set the frequency to "None".

![S3 Backup Settings in ERPNext](/files/s3_backup_settings.png)  





