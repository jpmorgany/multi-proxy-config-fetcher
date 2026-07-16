# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://www.v2nodes.com/subscriptions/country/all/?key=2BA5A971FC9B206",
    "https://raw.githubusercontent.com/sakha1370/OpenRay/refs/heads/main/output_iran/iran_top100_checked.txt",
    "https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/refs/heads/main/Countries/Iran.txt",
    "https://raw.githubusercontent.com/ThomasJasperthecat/sub/main/sublist1.txt",
    "https://raw.githubusercontent.com/hamedp-71/For_All_Net/refs/heads/main/hp.txt",
    "https://raw.githubusercontent.com/hamedp-71/Sub_Checker_Creator/refs/heads/main/final.txt",
    "https://raw.githubusercontent.com/masir-sefid/Sub/main/Telegram-Channel-@Masir_Sefid.txt",
    "https://raw.githubusercontent.com/igareck/vpn-configs-for-russia/refs/heads/main/BLACK_SS%2BAll_RUS.txt",
    "https://etoneya.su/1",
    "https://raw.githubusercontent.com/flaafix/AetrisVPN/refs/heads/main/AetrisVPN.txt",
    "https://raw.githubusercontent.com/flaafix/AetrisVPN-black-list/refs/heads/main/configs.txt",
    "https://raw.githubusercontent.com/flaafix/AetrisVPN-white-list-lite/refs/heads/main/AetrisVPN.txt",
    "https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/default/all.txt",
    "https://sub.proxygo.org/v2ray.php?key=7538c143e413c37e07d54038e95bd9f9",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/refs/heads/main/V2RAY_BASE64.txt",
    "https://mifa.world/ss",
    "https://mifa.world/trojan",
    "https://mifa.world/hysteria",
    "https://mifa.world/vmess",
    "https://mifa.world/vless",
    "https://mifa.world/other",
    "https://raw.githubusercontent.com/Delta-Kronecker/V2ray-Config/refs/heads/main/config/all_configs.txt",
    "https://freeproxydb.com/api/proxy/subscribe?country=&protocol=hysteria2&anonymity=&speed=0,60&https=0&count=500&subscribe_format=v2ray",
    "https://freeproxydb.com/api/proxy/subscribe?country=&protocol=vmess&anonymity=&speed=0,60&https=0&count=500&subscribe_format=v2ray",
    "https://freeproxydb.com/api/proxy/subscribe?country=&protocol=vless&anonymity=&speed=0,60&https=0&count=500&subscribe_format=v2ray",
    "https://freeproxydb.com/api/proxy/subscribe?country=&protocol=trojan&anonymity=&speed=0,60&https=0&count=500&subscribe_format=v2ray",
    "https://freeproxydb.com/api/proxy/subscribe?country=&protocol=ss&anonymity=&speed=0,60&https=0&count=500&subscribe_format=v2ray",
    "https://freeproxydb.com/api/proxy/subscribe?country=&protocol=ssr&anonymity=&speed=0,60&https=0&count=500&subscribe_format=v2ray",
    "https://raw.githubusercontent.com/sakha1370/OpenRay/refs/heads/main/output/all_valid_proxies.txt",
    "https://raw.githubusercontent.com/LalatinaHub/Mineral/refs/heads/master/result/nodes",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vless.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vmess.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/trojan.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/ss.txt",
    "https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/other.txt",
    "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt",
    "https://sub.shadowproxy66.workers.dev/sub/104ea085-c4e8-498a-9988-f2d6acf2e070#ShadowProxy66(4)",
    "https://cdn.jsdelivr.net/gh/0xRadikal/Free-v2ray-Configs@main/all/configs_base64.txt",
    "https://raw.githubusercontent.com/aristapanell-cell/AriataPanel/refs/heads/main/config.yaml/combined/ALL/ALL.yaml",

]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = True

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 0

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "hy2://": True,	
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": True,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 1

# --- Sing-box Config Tester Settings ---

# Set to True to enable testing of configs using sing-box.
# If True, sing-box will be used to test all fetched configs and create a 'tested' config file.
# If False, the testing step will be skipped.
ENABLE_SINGBOX_TESTER = True

# Number of parallel workers to use for testing sing-box configs.
# A higher number means faster testing but uses more CPU/RAM.
SINGBOX_TESTER_MAX_WORKERS = 8

# Maximum time (in seconds) to wait for a sing-box config to respond during testing.
# Configs that take longer than this will be marked as failed.
SINGBOX_TESTER_TIMEOUT_SECONDS = 10

# List of URLs to test sing-box configs against.
# The tester will try each URL in order until one succeeds.
SINGBOX_TESTER_URLS = [
    'https://www.youtube.com/generate_204'
    #'https://www.gstatic.com/generate_204'
]

# --- Xray Config Tester Settings ---

# Set to True to enable testing of configs using Xray core.
# If True, Xray will be used to test all fetched configs before conversion and create a 'tested' config file.
# If False, the testing step will be skipped.
ENABLE_XRAY_TESTER = True

# Number of parallel workers to use for testing Xray configs.
# A higher number means faster testing but uses more CPU/RAM.
XRAY_TESTER_MAX_WORKERS = 8

# Maximum time (in seconds) to wait for an Xray config to respond during testing.
# Configs that take longer than this will be marked as failed.
XRAY_TESTER_TIMEOUT_SECONDS = 10

# List of URLs to test Xray configs against.
# The tester will try each URL in order until one succeeds.
XRAY_TESTER_URLS = [
    'https://www.youtube.com/generate_204'
    #'https://www.gstatic.com/generate_204'
]

# --- Location API Settings ---

# List of free IP geolocation APIs to identify server countries.
# The system tries APIs in order from top to bottom (first = highest priority).
# If one API fails or is rate-limited, the system automatically tries the next one.
#
# HOW TO ADD AN API:
# Simply add the domain name or full URL. Examples:
#   freeipapi.com
#   ip-api.com
#   https://ipapi.co
#   api.iplocation.net
#
# The system automatically detects the correct API format and endpoint.
# No API key is required for the APIs listed below.
#
# RECOMMENDED FREE APIs (ranked by reliability and rate limits):
#
# 1. freeipapi.com - 60 requests/minute, very fast, no registration
# 2. ip-api.com - 45 requests/minute, very reliable, widely used
# 3. ipapi.co - 1000 requests/day (~30k/month), good accuracy
# 4. ipwhois.app - 10000 requests/month, decent speed
# 5. api.iplocation.net - unlimited, fast, accurate
#
LOCATION_APIS = [
    'api.iplocation.net',
    'freeipapi.com',
    'ip-api.com',
    'ipapi.co'
]
