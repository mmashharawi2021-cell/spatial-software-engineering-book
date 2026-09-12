from pydantic import BaseModel, Field
class SpatialQuery(BaseModel):
    radius_m: float = Field(gt=0, le=5000)
    limit: int = Field(default=100, ge=1, le=500)
