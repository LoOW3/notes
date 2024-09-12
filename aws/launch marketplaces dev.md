```bash
#!/bin/bash

# 1
curl -X POST -d '{}' "https://webhooks.amplify.us-east-1.amazonaws.com/prod/webhooks?id=761e94c4-7f11-4265-8729-07e1ceb3a312&token=3dNfFEubyl2zlPUegEpIiMhSI29K9YsG6gUST41Mlg&operation=startbuild" -H "Content-Type:application/json"

# 2
curl -X POST -d '{}' "https://webhooks.amplify.us-east-1.amazonaws.com/prod/webhooks?id=e6dd84d1-4db4-4ec6-8b68-e6003f2d18e9&token=3BZisEEdriO8ry5HI1t0vjbwp5fyyZ9pY00iQ6uu9xg&operation=startbuild" -H "Content-Type:application/json"

# 3
curl -X POST -d '{}' "https://webhooks.amplify.us-east-1.amazonaws.com/prod/webhooks?id=4eb0fedf-abe0-465b-8a53-4f733b1511b7&token=apTHP0P7V3T74YHbyDjSwUrejYKnK9LYF3FtiISI6Q&operation=startbuild" -H "Content-Type:application/json"

echo "all good"

```