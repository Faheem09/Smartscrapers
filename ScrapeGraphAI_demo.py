import os
import json # Import the json module
import pandas as pd
from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info
import nest_asyncio # Import nest_asyncio

# openai_key = os.getenv("OPENAI_APIKEY")
openai_key = "<<<YOUR_OPENAI_APIKEY HERE>>>"
graph_config = {
   "llm": {
      "api_key": openai_key,
      "model": "gpt-3.5-turbo",
   },
}

# ************************************************
# Create the SmartScraperGraph instance and run it
# ************************************************

smart_scraper_graph = SmartScraperGraph(
   prompt="List me all the projects with their description.",
   # also accepts a string with the already downloaded HTML code
   source="https://perinim.github.io/projects/",
   config=graph_config
)

nest_asyncio.apply() # Apply nest_asyncio to allow nested event loops
result = smart_scraper_graph.run()
print(result)

# Pretty print the JSON result
print(json.dumps(result, indent=4))

# Assuming 'result' is the dictionary containing the extracted data
df = pd.DataFrame(result['projects'])

print(df)
