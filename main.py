import json
from modules.resource_collection import MainResourceGather

with open('./settings.json') as config:
    settings = json.load(config)

# Run resource collection
MainResourceGather().mainloop()
