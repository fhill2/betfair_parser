from betfair_parser.spec.accounts.enums import IncludeItem, Wallet
from betfair_parser.spec.accounts.type_definitions import (
    AccountDetailsResponse,
    AccountFundsResponse,
    AccountStatementReport,
    CurrencyRate,
)
from betfair_parser.spec.common import BaseMessage, Request, Response, TimeRange


class getAccountFunds(Request, kw_only=True, frozen=True):
    """Returns the available to bet amount, exposure and commission information."""

    method = "AccountAPING/v1.0/getAccountFunds"
    params: dict = {}
    return_type = Response[AccountFundsResponse]


class getAccountDetails(Request, kw_only=True, frozen=True):
    """Returns the details relating your account, including your discount rate and Betfair point balance."""

    method = "AccountAPING/v1.0/getAccountDetails"
    params: dict = {}
    return_type = Response[AccountDetailsResponse]


class getAccountStatementParams(BaseMessage, frozen=True):
    locale: str | None = None  # The language to be used where applicable. Defaults to account settings
    fromRecord: int | None = None  # Specifies the first record that will be returned, defaults to 0
    recordCount: int | None = None  # Specifies the maximum number of records to be returned. Maximum 100

    # Return items with an itemDate within this date range. Both from and to date times are inclusive.
    # If from is not specified then the oldest available items will be in range. If to is not specified
    # then the latest items will be in range. nb. This itemDataRange is currently only applied when
    # includeItem is set to ALL or not specified, else items are NOT bound by itemDate.
    # Please note:  You can only retrieve account statement items for the last 90 days.
    itemDateRange: TimeRange | None = None
    includeItem: IncludeItem | None = None  # Which items to include, if not specified then defaults to ALL.
    wallet: Wallet | None = None  # Which wallet to return statementItems for. Defaults to UK


class getAccountStatement(Request, kw_only=True, frozen=True):
    method = "AccountAPING/v1.0/getAccountStatement"
    params: getAccountStatementParams
    return_type = AccountStatementReport


class listCurrencyRatesParams(BaseMessage, frozen=True):
    fromCurrency: str | None = None  # The currency from which the rates are computed. Only GBP for now.


class listCurrencyRates(Request, kw_only=True, frozen=True):
    """Returns a list of currency rates based on given currency. Updates only once per hour."""

    method = "AccountAPING/v1.0/listCurrencyRates"
    return_type = list[CurrencyRate]
