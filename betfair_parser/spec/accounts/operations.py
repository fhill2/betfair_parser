from typing import Optional

from betfair_parser.spec.accounts.enums import IncludeItem, Wallet
from betfair_parser.spec.accounts.type_definitions import (
    AccountDetailsResponse,
    AccountFundsResponse,
    AccountStatementReport,
    CurrencyRate,
)
from betfair_parser.spec.common import APIException, BaseMessage, Request, Response, TimeRange
from betfair_parser.spec.error import AccountAPIExceptionCode


AccountAPIException = APIException[AccountAPIExceptionCode]


class _GetAccountFundsParams(BaseMessage, frozen=True):
    wallet: Optional[Wallet] = None  # Name of the wallet in question. Global wallet is returned by default


class GetAccountFunds(Request, kw_only=True, frozen=True):
    """Returns the available to bet amount, exposure and commission information."""

    method = "AccountAPING/v1.0/getAccountFunds"
    params: _GetAccountFundsParams
    return_type = Response[AccountFundsResponse]
    throws = AccountAPIException


class GetAccountDetails(Request, kw_only=True, frozen=True):
    """Returns the details relating your account, including your discount rate and Betfair point balance."""

    method = "AccountAPING/v1.0/getAccountDetails"
    return_type = Response[AccountDetailsResponse]
    throws = AccountAPIException


class _GetAccountStatementParams(BaseMessage, frozen=True):
    locale: Optional[str] = None  # The language to be used where applicable. Defaults to account settings
    from_record: Optional[int] = None  # Specifies the first record that will be returned, defaults to 0
    record_count: Optional[int] = None  # Specifies the maximum number of records to be returned. Maximum 100

    # Return items with an itemDate within this date range. Both from and to date times are inclusive.
    # If from is not specified then the oldest available items will be in range. If to is not specified
    # then the latest items will be in range. nb. This itemDataRange is currently only applied when
    # includeItem is set to ALL or not specified, else items are NOT bound by itemDate.
    # Please note:  You can only retrieve account statement items for the last 90 days.
    item_date_range: Optional[TimeRange] = None
    include_item: Optional[IncludeItem] = None  # Which items to include, if not specified then defaults to ALL.
    wallet: Optional[Wallet] = None  # Which wallet to return statementItems for. Defaults to UK


class GetAccountStatement(Request, kw_only=True, frozen=True):
    method = "AccountAPING/v1.0/getAccountStatement"
    params: _GetAccountStatementParams
    return_type = Response[AccountStatementReport]
    throws = AccountAPIException


class _ListCurrencyRatesParams(BaseMessage, frozen=True):
    from_currency: Optional[str] = None  # The currency from which the rates are computed. Only GBP for now.


class ListCurrencyRates(Request, kw_only=True, frozen=True):
    """Returns a list of currency rates based on given currency. Updates only once per hour."""

    method = "AccountAPING/v1.0/listCurrencyRates"
    params: _ListCurrencyRatesParams
    return_type = Response[list[CurrencyRate]]
    throws = AccountAPIException