// raw dataset 
const url = (
    "https://raw.githubusercontent.com/sunse-kwon/ormi-dev-project-1/master/data/TOURISM.csv"
    )
// chatGPT API
const baseurl = "https://estsoft-openai-api.jejucodingcamp.workers.dev"

sessionStorage.setItem('rawURL', JSON.stringify(url))
sessionStorage.setItem('baseURL', JSON.stringify(baseurl))