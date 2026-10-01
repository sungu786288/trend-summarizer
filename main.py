import requests
import json
from datetime import datetime

def fetch_trending_ai_repos():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "topic:ai created:>" + (datetime.now().strftime('%Y-%m-%d')),
        "sort": "stars",
        "order": "desc",
        "per_page": 5
    }
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json().get("items", [])

def generate_summary(repos):
    lines = ["# AI Trending Repos", "", "Generated on " + datetime.now().strftime('%Y-%m-%d'), ""]
    for repo in repos:
        name = repo.get("full_name", "")
        desc = repo.get("description") or "No description"
        stars = repo.get("stargazers_count", 0)
        url = repo.get("html_url", "")
        lines.append(f"## {name}")
        lines.append(f"- Stars: {stars}")
        lines.append(f"- Description: {desc}")
        lines.append(f"- URL: {url}")
        lines.append("")
    return "\n".join(lines)

def main():
    try:
        repos = fetch_trending_ai_repos()
        summary = generate_summary(repos)
        print(summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
