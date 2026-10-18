import os

import pytest
from playwright.sync_api import sync_playwright

from config.settings import BASE_URL
from pages.login_page import LoginPage
from test_data.test_users import STANDARD_PASSWORD, STANDARD_USERNAME


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    p = context.new_page()
    yield p
    context.close()


@pytest.fixture
def authenticated_page(page):
    login_page = LoginPage(page)
    login_page.open(BASE_URL)
    login_page.login(STANDARD_USERNAME, STANDARD_PASSWORD)
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is None:
            page = item.funcargs.get("authenticated_page")
        if page is not None:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")
            try:
                page.screenshot(path=screenshot_path, full_page=True)
                print(f"\nFailure screenshot saved: {screenshot_path}")
            except Exception as error:  # pragma: no cover
                print(f"\nCould not capture screenshot: {error}")


import os
import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page is None:
            page = item.funcargs.get("authenticated_page")

        if page is not None:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = os.path.join(
                "screenshots",
                f"{item.name}.png"
            )

            try:
                page.screenshot(
                    path=screenshot_path,
                    full_page=True
                )
                print(f"\nFailure screenshot saved: {screenshot_path}")
            except Exception as error:
                print(f"\nCould not capture screenshot: {error}")

import os
from datetime import datetime

import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")

    if page is None:
        page = item.funcargs.get("authenticated_page")

    if page is None:
        return

    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = "".join(
        character if character.isalnum() or character in "-_" else "_"
        for character in item.name
    )

    screenshot_path = os.path.join(
        "screenshots",
        f"{safe_name}_{timestamp}.png"
    )

    log_path = os.path.join(
        "logs",
        f"{safe_name}_{timestamp}.txt"
    )

    try:
        page.screenshot(path=screenshot_path, full_page=True)

        with open(log_path, "w", encoding="utf-8") as log_file:
            log_file.write(f"Test: {item.nodeid}\n")
            log_file.write(f"URL: {page.url}\n")
            log_file.write(f"Title: {page.title()}\n")
            log_file.write(f"Screenshot: {screenshot_path}\n")
            log_file.write(f"Failure: {report.longreprtext}\n")

        print(f"\nScreenshot saved: {screenshot_path}")
        print(f"Failure details saved: {log_path}")

    except Exception as error:
        print(f"\nCould not save failure diagnostics: {error}")