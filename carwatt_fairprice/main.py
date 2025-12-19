from fastapi import FastAPI
from pricing.models import VehicleInput, MarketListing, FairPriceResponse
from pricing.engine import calculate_fair_price

app = FastAPI(title="CarWatt FairPrice™ API")

@app.post("/fairprice", response_model=FairPriceResponse)
def get_fair_price(
    vehicle: VehicleInput,
    comps: list[MarketListing]
):
    fair_price, confidence = calculate_fair_price(vehicle, comps)

    return FairPriceResponse(
        fair_price=fair_price,
        confidence_score=confidence,
        comps_used=len(comps),
    )