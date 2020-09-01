OES_APPL_VER_ID = "0.16.0.4"
OES_APPL_VER_VALUE = 1001600041
OES_MIN_APPL_VER_ID = "0.15.5"
OES_APPL_NAME = "OES"
OESMSG_ORD_NEW_ORDER = 0x01
OESMSG_ORD_CANCEL_REQUEST = 0x02
OESMSG_ORD_BATCH_ORDERS = 0x03
__OESMSG_RPT_MIN = 0x0F
OESMSG_RPT_MARKET_STATE = 0x10
OESMSG_RPT_REPORT_SYNCHRONIZATION = 0x11
OESMSG_RPT_BUSINESS_REJECT = 0x12
OESMSG_RPT_ORDER_INSERT = 0x13
OESMSG_RPT_ORDER_REPORT = 0x14
OESMSG_RPT_TRADE_REPORT = 0x15
OESMSG_RPT_FUND_TRSF_REJECT = 0x16
OESMSG_RPT_FUND_TRSF_REPORT = 0x17
OESMSG_RPT_CASH_ASSET_VARIATION = 0x18
OESMSG_RPT_STOCK_HOLDING_VARIATION = 0x19
OESMSG_RPT_OPTION_HOLDING_VARIATION = 0x1A
OESMSG_RPT_OPTION_SETTLEMENT_CONFIRMED = 0x1C
OESMSG_RPT_NOTIFY_INFO = 0x1E
OESMSG_RPT_SERVICE_STATE = 0x1F
__OESMSG_NONTRD_MIN = 0x20
OESMSG_NONTRD_FUND_TRSF_REQ = 0x21
OESMSG_NONTRD_CHANGE_PASSWORD = 0x22
OESMSG_NONTRD_OPT_CONFIRM_SETTLEMENT = 0x23
__OESMSG_QRYMSG_MIN = 0x2F
OESMSG_QRYMSG_CLIENT_OVERVIEW = 0x30
OESMSG_QRYMSG_STK_HLD = 0x34
OESMSG_QRYMSG_OPT_HLD = 0x35
OESMSG_QRYMSG_CUST = 0x36
OESMSG_QRYMSG_COMMISSION_RATE = 0x38
OESMSG_QRYMSG_FUND_TRSF = 0x39
OESMSG_QRYMSG_ETF = 0x3B
OESMSG_QRYMSG_ETF_COMPONENT = 0x3C
OESMSG_QRYMSG_OPTION = 0x3D
OESMSG_QRYMSG_ISSUE = 0x3E
OESMSG_QRYMSG_LOT_WINNING = 0x3F
OESMSG_QRYMSG_TRADING_DAY = 0x40
OESMSG_QRYMSG_MARKET_STATE = 0x41
OESMSG_QRYMSG_COUNTER_CASH = 0x42
OESMSG_QRYMSG_OPT_UNDERLYING_HLD = 0x43
OESMSG_QRYMSG_NOTIFY_INFO = 0x44
OESMSG_QRYMSG_OPT_POSITION_LIMIT = 0x45
OESMSG_QRYMSG_OPT_PURCHASE_LIMIT = 0x46
OESMSG_QRYMSG_BROKER_PARAMS = 0x48
OESMSG_QRYMSG_INV_ACCT = 0x51
OESMSG_QRYMSG_STOCK = 0x52
OESMSG_QRYMSG_CASH_ASSET = 0x53
OESMSG_QRYMSG_ORD = 0x54
OESMSG_QRYMSG_TRD = 0x55
OESMSG_QRYMSG_OPT_EXERCISE_ASSIGN = 0x56
OESMSG_SESS_HEARTBEAT = 0xFA
OESMSG_SESS_TEST_REQUEST = 0xFB
OESMSG_SESS_LOGIN_EXTEND = 0xFC
OESMSG_SESS_LOGOUT = 0xFE
OESMSG_RPT_ORDER_REJECT = OESMSG_RPT_BUSINESS_REJECT
OESMSG_QRYMSG_ORD_L001509 = 0x31
OESMSG_QRYMSG_TRD_L001509 = 0x32
OESMSG_QRYMSG_CASH_ASSET_L001509 = 0x33
OESMSG_QRYMSG_INV_ACCT_L001508 = 0x37
OESMSG_QRYMSG_STOCK_L001508 = 0x3A
OESMSG_QRYMSG_OPT_EXERCISE_ASSIGN_L001600 = 0x47
OES_SUB_RPT_TYPE_DEFAULT = 0
OES_SUB_RPT_TYPE_BUSINESS_REJECT = 0x01
OES_SUB_RPT_TYPE_ORDER_INSERT = 0x02
OES_SUB_RPT_TYPE_ORDER_REPORT = 0x04
OES_SUB_RPT_TYPE_TRADE_REPORT = 0x08
OES_SUB_RPT_TYPE_FUND_TRSF_REPORT = 0x10
OES_SUB_RPT_TYPE_CASH_ASSET_VARIATION = 0x20
OES_SUB_RPT_TYPE_HOLDING_VARIATION = 0x40
OES_SUB_RPT_TYPE_MARKET_STATE = 0x80
OES_SUB_RPT_TYPE_NOTIFY_INFO = 0x100
OES_SUB_RPT_TYPE_SETTLEMETN_CONFIRMED = 0x200
OES_SUB_RPT_TYPE_ALL = 0xFFFF
__MAX_OES_SUB_RPT_TYPE = 0x7FFFFFFF
OES_PROT_HINTS_TYPE_DEFAULT = 0
OES_PROT_HINTS_TYPE_COMPRESS = 0x80
OES_PROT_HINTS_TYPE_NONE = 0xFF
__MAX_OES_PROT_HINTS_TYPE = 0xFF