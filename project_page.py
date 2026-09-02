from playwright.sync_api import Page, expect

class ProjectPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_project(self, project_name):
        expect(self.page.get_by_text(project_name)).to_be_visible()
