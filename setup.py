#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
#if not os.access(usr_share, os.W_OK):
#    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-lite.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-lite.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum-lite.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum-lite.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-lite")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/background.png",
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="Electrum-Lite",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9', 'qt4'],
    package_dir={
        'electrum_lite': 'lib',
        'electrum_lite_gui': 'gui',
        'electrum_lite_plugins': 'plugins',
    },
    scripts=['electrum-lite'],
    data_files=data_files,
    py_modules=[
        'electrum_lite.account',
        'electrum_lite.bitcoin',
        'electrum_lite.blockchain',
        'electrum_lite.bmp',
        'electrum_lite.commands',
        'electrum_lite.i18n',
        'electrum_lite.interface',
        'electrum_lite.mnemonic',
        'electrum_lite.msqr',
        'electrum_lite.network',
        'electrum_lite.plugins',
        'electrum_lite.pyqrnative',
        'electrum_lite.simple_config',
        'electrum_lite.socks',
        'electrum_lite.transaction',
        'electrum_lite.util',
        'electrum_lite.verifier',
        'electrum_lite.version',
        'electrum_lite.wallet',
        'electrum_lite.wallet_bitkey',
        'electrum_lite.wallet_factory',
        'electrum_lite_gui.gtk',
        'electrum_lite_gui.qt.__init__',
        'electrum_lite_gui.qt.amountedit',
        'electrum_lite_gui.qt.console',
        'electrum_lite_gui.qt.history_widget',
        'electrum_lite_gui.qt.icons_rc',
        'electrum_lite_gui.qt.installwizard',
        'electrum_lite_gui.qt.lite_window',
        'electrum_lite_gui.qt.main_window',
        'electrum_lite_gui.qt.network_dialog',
        'electrum_lite_gui.qt.password_dialog',
        'electrum_lite_gui.qt.qrcodewidget',
        'electrum_lite_gui.qt.receiving_widget',
        'electrum_lite_gui.qt.seed_dialog',
        'electrum_lite_gui.qt.transaction_dialog',
        'electrum_lite_gui.qt.util',
        'electrum_lite_gui.qt.version_getter',
        'electrum_lite_gui.stdio',
        'electrum_lite_gui.text',
        'electrum_lite_plugins.aliases',
        'electrum_lite_plugins.coinbase_buyback',
        'electrum_lite_plugins.exchange_rate',
        'electrum_lite_plugins.labels',
        'electrum_lite_plugins.pointofsale',
        'electrum_lite_plugins.qrscanner',
        'electrum_lite_plugins.virtualkeyboard',
    ],
    description="Lightweight Litecoin Wallet",
    author="Daniel Cagara",
    author_email="contact@electrum-lite.org",
    license="GNU GPLv3",
    url="http://electrum-lite.org",
    long_description="""Lightweight Litecoin Wallet"""
)
