# API Keys & Credentials

Store all API keys here. Referenced by CLAUDE.md for any API calls.



## API calls

## Scrape LinkedIn Posts: Apify

endpoint: https://api.apify.com/v2/acts/supreme_coder~linkedin-post/run-sync-get-dataset-items?token=

body: {
    "deepScrape": false,
    "limitPerSource": 10,
    "rawData": false,
    "urls": [
        "https://www.linkedin.com/in/peterattiamd/",
        "https://www.linkedin.com/in/drhyman/"
    ]
}

## Image Generation

### Step 1: Request API

endpoint: https://queue.fal.run/fal-ai/nano-banana-pro

Authorization: Key 

body: {
  "prompt": "A professional customer service agent white young Asian girl/women, friendly expression, looking directly into the camera, 80% close-up to face, office background.",
  "aspect_ratio": "16:9",
  "duration": 8
}

### Step 2: Get Image Link

https://queue.fal.run/fal-ai/nano-banana-pro/requests/{{step1-request_id}}/status


## image upscale

import { fal } from "@fal-ai/client";

const result = await fal.subscribe("fal-ai/recraft/upscale/crisp", {
  input: {
    image_url: "https://storage.googleapis.com/falserverless/model_tests/recraft/recraft-upscaler-1.jpeg"
  },
  logs: true,
  onQueueUpdate: (update) => {
    if (update.status === "IN_PROGRESS") {
      update.logs.map((log) => log.message).forEach(console.log);
    }
  },
});
console.log(result.data);
console.log(result.requestId);

