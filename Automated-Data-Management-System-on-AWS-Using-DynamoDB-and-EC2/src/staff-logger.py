
import boto3# Create a DynamoDB resource using the us-east-1 region 

dynamodb= boto3.resource('dynamodb', region_name='us-east-1') # Reference your DynamoDB table 

table= dynamodb.Table('staff') # List of staff to add 

staff = [ {'StaffID': '001', 'name': 'Alice Appiah', 'Department': 'IT'}, 
             {'StaffID': '002', 'name': 'Rita Okai', 'Department': 'Finance'},
             {'StaffID': '003', 'name': 'Ansong Ampaw', 'Department': 'IT'}, 
             {'StaffID': '004', 'name': 'Rita Okloo', 'Department': 'Security'},
             {'StaffID': '005', 'name': 'Alice Mensah', 'Department': 'IT'}, 
             {'StaffID': '006', 'name': 'Rita Okloo', 'Department': 'Finance'},
             {'StaffID': '007', 'name': 'Philip Mensah', 'Department': 'IT'}, 
             {'StaffID': '008', 'name': 'Rita Yao', 'Department': 'Product'},
             {'StaffID': '009', 'name': 'Alice Appiah-Sarpong', 'Department': 'IT'}, 
             {'StaffID': '010', 'name': 'Akoto Richard', 'Department': 'Finance'}] 

# Loop through and insert each staff

for emp in staff: 
    response = table.put_item(Item=emp) 
    print(f"Inserted: {emp['name']} | Status: {response['ResponseMetadata']['HTTPStatusCode']}")