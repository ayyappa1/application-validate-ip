Analysis: 

Input: json request 
Url: http://ipinfo.io/json 

Response: 

{ 

  "ip": "27.5.240.224", 

  "city": "Chennai", 

  "region": "Tamil Nadu", 

  "country": "IN", 

  "loc": "13.0878,80.2785", 

  "org": "AS17488 Hathway IP Over Cable Internet", 

  "postal": "600001", 

  "timezone": "Asia/Kolkata", 

  "readme": "https://ipinfo.io/missingauth" 

} 
 
Validate response: 
Application code to get it’s own ip address 

Automation: 
Run unit test case on very commit in Circle CI 
 
 Prerequisites: 

 Github - Source code manager 

 Python - Implement application and test code 

 Circle’s CI  - Automate test case run on every commit 

Implementation: 

Application code 

Test application using test case module 

Use circle’s CI to automate process 

Conclusion: 

in CircleCI, jobs can be built using “circle.yaml” file whereas In Jenkins, builds are configured using web UI with setting option. 

In CircleCI has inbuilt support for parallelism whereas Jenkins can supports multiple jobs by multi-threading. 

In CircleCI has inbuilt support for docker whereas Jenkins we don’t have inbuilt support for docker, user need to install. 

CircleCI has the best feature for debugging “Debug via SSH”  
