import json
from modules.resources import MainResourceGather

with open('./settings.json') as config:
    settings = json.load(config)

# Run resource collection
MainResourceGather().mainloop()
