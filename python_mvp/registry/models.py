from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List

# Main data models for the registry system (not including the registry itself).

@dataclass
class Team:
	teams_id: int
	name: str
	created_at: datetime


