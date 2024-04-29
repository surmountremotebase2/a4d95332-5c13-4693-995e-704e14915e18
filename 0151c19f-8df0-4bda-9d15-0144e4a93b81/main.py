from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import RSI, EMA, SMA, MACD, MFI, BB
from surmount.logging import log

class TradingStrategy(Strategy):

    @property
    def assets(self):
        return ["MNQM2024"]

    @property
    def interval(self):
        return "5min"

    def run(self, data):
        d = data["ohlcv"]
        qqq_stake = 0
        if len(d)>3 and "13:00" in d[-1]["MNQM2024"]["date"]:
            v_shape = d[-2]["MNQM2024"]["close"]<d[-3]["MNQM2024"]["close"] and d[-1]["MNQM2024"]["close"]>d[-2]["MNQM2024"]["close"]
            log(str(v_shape))
            if v_shape:
                qqq_stake = 1

        return TargetAllocation({"MNQM2024": qqq_stake})