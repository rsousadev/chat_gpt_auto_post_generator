from pytrends.request import TrendReq


class GoogleTrends:
    def __init__(self) -> None:
        self._pytrend = TrendReq(
            hl="pt-BR",
            tz=-180,
            timeout=(10, 25),
            retries=3,
            backoff_factor=0.1,
            requests_args={"verify": True},
        )

    def search_trend(self) -> list:
        today_searches_df = self._pytrend.realtime_trending_searches(pn="BR")
        today_searches_df = today_searches_df["title"].values.tolist()
        return today_searches_df
