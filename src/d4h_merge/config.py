from __future__ import annotations

from configparser import ConfigParser
from pathlib import Path
import os


class Config:
    """Application configuration manager."""

    DEFAULTS = {
        "team_id": "426",
        "subdomain": "rosslandsar",
        "report_order": "4,5,3",
        "api_token": "",
        "output_folder": "",
    }

    def __init__(self) -> None:

        appdata = Path(
    os.environ.get(
        "APPDATA",
        Path.home() / "AppData" / "Roaming",
    )
)

self.app_folder = appdata / "D4H Merge"
self.app_folder.mkdir(parents=True, exist_ok=True)

self.settings_file = self.app_folder / "settings.ini"

        self.settings_file = self.app_folder / "settings.ini"

        self.parser = ConfigParser()

        if self.settings_file.exists():
            self.parser.read(self.settings_file)

        if "General" not in self.parser:
            self.parser["General"] = {}

        self._ensure_defaults()

    def _ensure_defaults(self) -> None:

        changed = False

        for key, value in self.DEFAULTS.items():
            if key not in self.parser["General"]:
                self.parser["General"][key] = value
                changed = True

        if changed:
            self.save()

    def save(self) -> None:

        with self.settings_file.open("w", encoding="utf-8") as f:
            self.parser.write(f)

    @property
    def api_token(self) -> str:
        return self.parser["General"]["api_token"]

    @api_token.setter
    def api_token(self, value: str) -> None:
        self.parser["General"]["api_token"] = value

    @property
    def team_id(self) -> int:
        return int(self.parser["General"]["team_id"])

    @team_id.setter
    def team_id(self, value: int) -> None:
        self.parser["General"]["team_id"] = str(value)

    @property
    def subdomain(self) -> str:
        return self.parser["General"]["subdomain"]

    @subdomain.setter
    def subdomain(self, value: str) -> None:
        self.parser["General"]["subdomain"] = value.strip()

    @property
    def report_order(self) -> list[int]:

        value = self.parser["General"]["report_order"]

        return [
            int(x.strip())
            for x in value.split(",")
            if x.strip()
        ]

    @report_order.setter
    def report_order(self, reports: list[int]) -> None:

        self.parser["General"]["report_order"] = ",".join(
            str(x) for x in reports
        )

    @property
    def output_folder(self) -> str:
        return self.parser["General"]["output_folder"]

    @output_folder.setter
    def output_folder(self, value: str) -> None:
        self.parser["General"]["output_folder"] = value