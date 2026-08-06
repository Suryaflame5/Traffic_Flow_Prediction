from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class PredictionInput(BaseModel):
    Hour: int = 14
    DayOfWeek: str = "Monday"
    IsHoliday: str = "No"
    WeatherCondition: str = "Clear"
    IntersectionID: str = "A"

class PredictionResponse(BaseModel):
    success: bool
    prediction: Any
    latency_ms: float

class HistoryLog(BaseModel):
    id: int
    timestamp: str
    input_data: Dict[str, Any]
    prediction: Any
    latency_ms: float
