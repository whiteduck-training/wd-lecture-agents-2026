"""Tiny in-memory issue tracker for agent workshop exercises."""

from dataclasses import dataclass


@dataclass
class Issue:
    id: int
    title: str
    priority: str = "medium"
    status: str = "open"


class IssueTracker:
    def __init__(self) -> None:
        self._issues: list[Issue] = []
        self._next_id = 1

    def create(self, title: str, priority: str = "medium") -> Issue:
        issue = Issue(id=self._next_id, title=title.strip(), priority=priority)
        self._issues.append(issue)
        self._next_id += 1
        return issue

    def list_open(self) -> list[Issue]:
        return [issue for issue in self._issues if issue.status == "open"]

    def close(self, issue_id: int) -> Issue:
        issue = self._find(issue_id)
        issue.status = "closed"
        return issue

    def search(self, text: str) -> list[Issue]:
        needle = text.strip().lower()
        return [issue for issue in self._issues if needle in issue.title.lower()]

    def next_issue(self) -> Issue | None:
        open_issues = self.list_open()
        if not open_issues:
            return None
        return sorted(open_issues, key=lambda issue: issue.priority)[0]

    def _find(self, issue_id: int) -> Issue:
        for issue in self._issues:
            if issue.id == issue_id:
                return issue
        raise KeyError(f"Unknown issue id: {issue_id}")
