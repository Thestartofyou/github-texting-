from github import Github

# Replace with your GitHub personal access token
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Create a GitHub instance
github = Github(ACCESS_TOKEN)

# Replace with the repository owner, repository name, and issue number
repo_owner = "owner_username"
repo_name = "repository_name"
issue_number = 123

# Create a repository object
repo = github.get_repo(f"{repo_owner}/{repo_name}")

# Add a comment to the issue
comment_text = "This is a test comment from the script."
issue = repo.get_issue(issue_number)
issue.create_comment(comment_text)

print("Comment posted successfully.")
