## Build Container Image

gcloud builds submit --tag gcr.io/personal-279606/font3d

## Deploy to Google Cloud Run

gcloud run deploy --image gcr.io/personal-279606/font3d --platform managed
