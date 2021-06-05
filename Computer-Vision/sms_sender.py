#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

import datetime
date = datetime.datetime.now() 
def sendsms():
    account_sid = "ACdcfae8e5c4069d3cb80385ce2d36c855"
    auth_token = "ccef4133311775065451e4b028c7d296"
    client = Client(account_sid, auth_token)

    message = client.messages                     .create(
                         body=f"Face detected at {date}",
                         from_='+12407248231',
                         to='+91 7350365576'
                     )

    print(f"Messaged successfully !!")


# In[ ]:





# In[ ]:





# In[ ]:




