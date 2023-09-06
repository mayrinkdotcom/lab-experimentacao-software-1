import os
from graphqlclient import GraphQLClient
from datetime import datetime as date
import json
import csv
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

dadosArquivo = open('dados.csv', 'w', newline='')

url = "https://api.github.com/graphql"
token = API_TOKEN
today = date.utcnow()
variables = {}

client = GraphQLClient(url)
client.inject_token(token=token)

end_cursor = 'null'
i = 1
writer = csv.writer(dadosArquivo)
header = [
    "Name",
    "URL",
    "Stargazers",
    "Created At",
    "Age", 
    "Pull Requests",
    "Language",
    "Updated At",
    "Days Since Update",
    "Releases",
    "Closed Issues",
    "Total Issues",
    "Issues Ratio"
]
writer.writerow(header)
while i < 1000:
    query = """
            query {
              search(query: "is:public stars:>1600 sort:stars", type: REPOSITORY, first: 20, after: """ + end_cursor + """) {
                pageInfo{
                  hasNextPage
                  endCursor
                }
                nodes {
                  ... on Repository {
                    stargazerCount
                    nameWithOwner
                    url
                    createdAt
                    pullRequests(states: MERGED) { totalCount }
                    primaryLanguage { name }
                    updatedAt
                    releases { totalCount }
                    closedIssues: issues(states: CLOSED) { totalCount }
                    totalIssues: issues { totalCount }
                  }
                }
              }
            }
            """
    
    try:
      data = json.loads(client.execute(query=query, variables=variables))
      results = data["data"]["search"]
    except:
      print("Falha! Tentando novamente...")
      continue
    end_cursor = '"' + results["pageInfo"]["endCursor"] + '"'

    variables["after"] = end_cursor
    repositories = results["nodes"]
    
    

    for repo in repositories:
        name = repo["nameWithOwner"]
        url = repo["url"]
        created_at = date.strptime(repo["createdAt"], "%Y-%m-%dT%H:%M:%SZ")
        age = (today - created_at).days
        pull_requests = repo["pullRequests"]["totalCount"]
        language = repo["primaryLanguage"]["name"] if repo["primaryLanguage"] is not None else "none"
        updated_at = date.strptime(repo["updatedAt"], "%Y-%m-%dT%H:%M:%SZ")
        days_since_update = (today - updated_at).days
        releases = repo["releases"]["totalCount"]
        closed_issues = repo["closedIssues"]["totalCount"]
        total_issues = repo["totalIssues"]["totalCount"]
        issues_ratio = closed_issues / total_issues if total_issues > 0 else 0
        stargazers_count = repo["stargazerCount"]

        print("Index: " + str(i))
        row = [
          name,
          url,
          stargazers_count,
          created_at,
          age,
          pull_requests,
          language,
          updated_at,
          days_since_update,
          releases,
          closed_issues,
          total_issues,
          issues_ratio
        ]
        writer.writerow(row)
        i = i + 1

print(15 * "-" + "FIM" + 15 * "-")

dadosArquivo.close()