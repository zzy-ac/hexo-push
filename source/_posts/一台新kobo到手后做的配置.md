---
title: 一台新kobo到手后做的配置
date: 2022-01-10 20:15:41
tags: kobo
keywords:
categories: kobo
---

# 一台新kobo到手后做的配置：





## 一、激活：

打开数据库，往user数据里写入userid和useremail



## 二、更新固件

在[这个网站](https://pgaskin.net/KoboStuff/kobofirmware.html)下载对应型号的对应版本的固件包，将其中的upgrade文件夹和KoboRoot.tgz文件解压到.kobo目录。拔线更新。

## 三、刷插件

### 1、NikelMenu

在[这个项目](https://github.com/pgaskin/NickelMenu)releases里下载最新的插件包并安装

在.add目录下创建文本文件并写入对应的脚本内容例如：

```
  menu_item :main   :Reboot   :power      :reboot

  menu_item :main :KOReader :cmd_spawn :quiet:/mnt/onboard/.adds/koreader/koreader.sh
  menu_item :main   :Rescan_Books  :nickel_misc  :rescan_books
  menu_item :main   :Font-OLD :cmd_spawn :quiet:/mnt/onboard/.adds/freefont/old.sh
  menu_item :main   :Font-NEW :cmd_spawn :quiet:/mnt/onboard/.adds/freefont/new.sh
```

### 2、NanoClock

按照[这个教程](https://www.mobileread.com/forums/showthread.php?t=340047)把nanoclock装入系统并自己配置好时钟的坐标、字体、大小等信息如：

```
; -------------------------------------------------------------------
;   NanoClock config file.
;   Canonical location: .adds/nanoclock/nanoclock.ini
; -------------------------------------------------------------------

[global]
;
; To uninstall, set to true
;
uninstall=false

;
; To temporarily stop displaying the clock, set to true
;
stop=false

;
; To debug, set to true
;; NOTE: Everything is sent to the syslog, to look specifically for nanoclock entries, run
;;       logread | grep '\(nanoclock\|nanoclock\.sh\)\[[[:digit:]]\+\]'
;; NOTE: Alternatively, you can find a NickelMenu config that will dump it in .adds/nanoclock/nanoclock.log
;;       over here: https://github.com/NiLuJe/NanoClock/blob/master/config/nm_nanoclock
;
debug=false

;
; If this is enabled, the current log will be dumped to .adds/nanoclock/nanoclock.log
; every time this config file is reloaded.
; This is a poor man's hack to get at the logs when you truly have no other way...
;
dump_log=false


[display]
;
; Date format string (see 'man strftime', e.g., <https://man7.org/linux/man-pages/man3/strftime.3.html>)
;
;; In addition may also use {month}, {day}, {battery}.
;; (Look for battery and locale settings further below).
;
format=%H:%M

;
; In addition to the usual "as necessary" refreshes,
; also refresh the clock automatically, every minute, on the dot.
; Set to false to disable.
;;
;; NOTE: If the device is not connected to a power source, and Wi-Fi is currently down,
;;       the device will be put into standby after roughly 5s of inactivity.
;;       That's essentially a suspend to RAM, but with the lights & touch panel still on.
;;       This means that, despite this setting, your clock will "freeze" very soon after a page turn,
;;       until the next sign of user activity (e.g., a touch or button press),
;;       at which point the device wakes up and everything resumes.
;;
;
autorefresh=1


;
; Where to print the clock
;

;
; With one of the embedded bitmap fonts:
;
column=-14
row=-1
;; ^NOTE: Can be negative (f.g., row -1 is the last line of the screen (bottom), column -1 is the last column on the screen (right)).
offset_x=-2
offset_y=-8
;; ^NOTE: These do *NOT* override row/column, they *fine-tune* them. Offsets can be negative, but will not wrap around edges.
;;       f.g., if you only print a %H:%M timestamp, that's 5 characters, so, the bottom-right corner of the screen would be:
;;       column=-5
;;       row=-1
;;       You can then adjust that a bit, by, say, moving it 10 pixels higher:
;;       offset_y=-10
;;  NOTE: While column/row won't, offset_x/offset_y *can* push content off-screen!

;
; Font:  (IBM, UNSCII, ALT, THIN, FANTASY, MCR, TALL, BLOCK,
;         LEGGIE, VEGGIE, KATES, FKP, CTRLD, ORP, ORPB, ORPI,
;         SCIENTIFICA, SCIENTIFICAB, SCIENTIFICAI, TERMINUS,
;         TERMINUSB, FATTY, SPLEEN, TEWI, TEWIB, TOPAZ,
;         MICROKNIGHT, VGA, COZETTE)
;
font=IBM

;
; Font Size:
; NOTE: This is an integer multiplier of the native cell size of the font. (0 means choose a sensible default based on DPI, ranging from 2 to 4).
;
size=0

;
; Color: (BLACK GRAY{1-9A-E} WHITE)
;
fg_color=BLACK
bg_color=WHITE
;

;
; With your own vector (TrueType, OpenType) fonts:
;
;; For fonts inside the same folder as your NanoClock configuration:
;;     truetype=yourfont.ttf
;
;; For fonts stored elsewhere in the filesystem:
;;     truetype=/mnt/onboard/fonts/something.ttf
;
;; Only set these if you use *italic*, **bold**, ***bold italic*** in your format string:
;;
;;     truetype_format=*%a* **%b** ***%d*** %H:%M
;;     truetype_bold=yourfont-bold.ttf
;;     truetype_italic=yourfont-italic.ttf
;;     truetype_bolditalic=yourfont-bolditalic.ttf
;
;; Technically, this can also be used for completely different font styles,
;; instead of italic or bold variants of the same font.
;
;; NOTE: Will fall back to regular mode when font file is unavailable.
;;       (e.g. while the device is connected to USB)
;
#truetype_size=16.0
#truetype_px=0
;; ^NOTE: size is in pt, px is in pixels. If set to non-zero, px takes precedence.
;;        In case you ever need to do the maths yourself, px = dpi / 72.0 * pt
#truetype_x=0
#truetype_y=0
;; ^NOTE: Much like above, these can be negative, in which case they count backwards from the opposite edge (like column/row).
;;        f.g., a rough match to the column/row example above might be:
;;        truetype_x=-115
;;        truetype_y=-44
;;
;; NOTE:  If you want to position your clock near the bottom or right edge,
;;        using negative values is the only sensible way to have it actually work in both Portrait and Landscape orientations,
;;        whether you're using a vector or a bitmap font.
;;
truetype_fg=BLACK
truetype_bg=WHITE

;
; TrueType padding
;
;; TrueType padding helps prevent visual fragments to appear,
;; in the extremely rare instance of multiple clock updates on the same page,
;; but it comes at the cost of adding extra whitespace.
;; Set to true to enable.
;; NOTE: If you still have this enabled, and you're seeing weird layout issues on the first update after a truetype switch,
;;       try disabling it.
;; NOTE: This setting is mostly meaningless if backgroundless or overlay are enabled, but it is still honored,
;;       as it might help the autorefresh magic behave seamlessly ;).
;
truetype_padding=true
truetype=/mnt/onboard/fonts/Roboto-Regular.ttf
# truetype_format=%a %b %d %H:%M
truetype_format={battery}|%H:%M
truetype_size=16.0
truetype_px=20
truetype_x=650
truetype_y=980
;
; Misc display tweaks (regardless of the font type)
;
;; Don't render background pixels *at all* (i.e., no background "box").
;; Set to true to enable.
backgroundless=0
;; Ignores the specified foreground color, and instead use the inverse of what's on the screen.
;; (f.g., if a pixel replaces a white pixel, it'll be painted black).
;; Like with backgroundless, background pixels won't be rendered. Takes precedence over backgroundless.
;; Set to true to enable.
overlay=false
;; ^NOTE: If autorefresh is enabled, magic will happen to make these two behave without visual glitches ;).
;; ^NOTE: On devices with a sunxi SoC (e.g., Mk. 8), these two modes are unavailable, because of technical limitations.

;
; Battery percentage value (0-100)
;
;; Use {battery} in the format string.
;
;; Will only be used if the battery is between min max.
;; Default: only shown when battery level drops to 50% and under.
battery_min=0
battery_max=100
;
;; Allows tweaking how the placeholder is formatted.
;; %d will be replaced by the actual value
;; %% is a literal % sign
;; The default is to show nothing when hidden, and an unadorned percentage otherwise.
; When the battery is shown (i.e., within the configured threshold)
;;battery_shown_pattern=%d%%
; When the battery is hidden (i.e., outside the configured threshold)
;;battery_hidden_pattern=
;
; For example, if you want to display the battery between brackets as a prefix to your clock,
; but don't want those brackets to mess up your formatting when the battery is *NOT* shown:
; format={battery} %H:%M
; battery_shown_pattern=[%d%%]
; battery_hidden_pattern=
; (Note that in a config value, leading spaces will be ignored, but not *trailing* spaces,
;  so you may also use '{battery}%H:%M' for format and '[%d%%] ' for battery_shown_pattern).

;
; Localization (translate Month and Day names)
;
;; Set day names, Monday -> Sunday (7 words)
;; Use {day} in the format string to use this.
;
;days=Mon Tue Wed Thu Fri Sat Sun
;
;; Set month names, January -> December (12 words)
;; Use {month} in the format string to use this.
;
;months=Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
;

;
; Frontlight percentage value (0-100 or -1)
;
;; Use {frontlight} in the format string.
;; ^NOTE: It might take a couple pages to sync up on older devices (< Mk. 7). That's perfectly normal.
;
;; Allows tweaking how the placeholder is formatted.
;; c.f., the description for {battery} above for more details.
;; The default is to show an unadorned percentage.
frontlight_pattern=%d%%
```

### 3、Koreader

直接从[koreader项目](https://github.com/koreader/koreader)把kobo版的koreader下下来把其中的koreader文件夹解压到.add目录，见上文的nikelmenu部分添加启动koreader的按钮

### 4、KoboPatch

从[这个教程](https://www.mobileread.com/forums/showthread.php?t=297338)中安装kobopatch到电脑，并编写kobopatch.yaml来选择需要的补丁功能

```yaml
## Works with kobopatch v0.15.0 and later.
## You can update kobopatch by downloading the latest release from https://github.com/pgaskin/kobopatch/releases. 
version: 4.30.18838
in: src/kobo-update-4.30.18838.zip
out: out/KoboRoot.tgz
log: out/log.txt

patchFormat: kobopatch

patches:
  src/nickel.yaml: usr/local/Kobo/nickel
  src/libadobe.so.yaml: usr/local/Kobo/libadobe.so
  src/libnickel.so.1.0.0.yaml: usr/local/Kobo/libnickel.so.1.0.0
  src/librmsdk.so.1.0.0.yaml: usr/local/Kobo/librmsdk.so.1.0.0

## You can put lines in the following section to override the enabled state of patches.
## The indentation matters! Each override should be indented by 4 spaces. Add to the 
## section below. This section can be copy and pasted into newer patch versions to
## keep your selections.
##
## Example of how it should look:
## overrides:
##   src/nickel.yaml:
##     Custom synopsis/details line spacing: yes
##     Whatever the yaml is called: no
##   src/libadobe.so.yaml:
##     You get the idea: yes
overrides:
  src/nickel.yaml:
    Reduce top/bottom page spacer: yes
    # Custom synopsis details line spacing: yes
    # Custom synopsis font size: yes
    # Increase home screen cover size: yes
    Dictionary pop-up - increase available text area: yes
    # Increase Book Details synopsis area: yes
    Increase library cover size: yes
    # Custom collection/author header title font: yes
    # Reduce new header/footer height: yes
    # Custom header/footer captions: yes
    # Custom page navigation scrubber: yes
    Customise Header back button: yes
    # Series list increase cover thumbnails: yes
    # Increase headlines font: yes
    # New home screen subtitle custom font: yes
    Remove footer (row3) and increase cover size on new home screen: yes
    # Remove footer (row3) on new home screen: yes
    # Show all games: yes
    # Remove forgot pin button from lock screen: yes
    Increase size of kepub chapter progress chart: yes
    Change TOC level indentation: yes
  src/libadobe.so.yaml:
    # Remove PDF map widget shown during panning: yes
  src/libnickel.so.1.0.0.yaml:
    # My 10 line spacing values: yes
    # My 24 line spacing values: yes
    Custom left & right margins: yes
    # Custom font sizes: yes
    # ePub fixed top/bottom margins: yes
    # ePub disable built-in body padding-bottom: yes
    Custom kepub default margins: yes
    # Block WiFi firmware upgrade: yes
    Custom Sleep/Power-off timeouts: yes
    Set KePub hyphenation: yes
    # Force user line spacing in KePubs: yes
    # Force user line spacing in ePubs (part 1 of 2): yes
    Un-force font-family override p tags (std epubs): yes
    # Force user font-family in ePubs (Part 1 of 2): yes
    # ePub constant font sharpness: yes
    # KePub constant font sharpness: yes
    Un-Force user text-align in div,p tags in KePubs: yes
    Un-Force user font-family in KePubs: yes
    Un-force link decoration in KePubs: yes
    # Ignore .otf fonts: yes
    Dictionary text font-family/font-size/line-height: yes
    # Custom navigation menu page number text: yes
    KePub stylesheet additions - text justify: yes
    # KePub stylesheet additions - optimizeSpeed: yes
    # Shorten dictionary entry not found message: yes
    # Change Wikipedia search language: yes
    # Cyrillic Keyboard (GloHD/ClaraHD/AuraOne/H2O2): yes
    # Greek Keyboard (GloHD/ClaraHD/AuraOne/H2O2): yes
    # Bulgarian Phonetic Keyboard (GloHD/ClaraHD/AuraOne/H2O2/Forma/Libra): yes
    # Don't grab exclusive access to event0: yes
    # Both page turn buttons go next: yes
    # Both page turn sides go next: yes
    # Increase page navigation history: yes
    # Replace adobe page numbers toggle with invert screen: yes
    # Always show confirmation dialog before upgrading: yes
    # Allow USB storage even when device locked: yes
    # Hide browser from beta features: yes
    # Remove beta features not supported text: yes
    Disable all tutorial dialogs: yes
    # Remove recommendations (row1col2) from home screen: yes
    # Rename new home screen footer: yes
    # Remove line from bottom tab bar: yes
    # Change Browse Kobo home screen link target - Activity: yes
    # Set visible SmartLink: yes
    # Only show Pocket SmartLink: yes
    # Only show stats SmartLink: yes
    Never show Kobo Plus, wishlist, and points SmartLinks: yes
    # Allow showing info panel on random screensaver: yes
    Remove title from reading header/footer: yes
    # Larger Sleep/Power-off timeouts: yes
    # Allow rotation on all devices: yes
    # Don't uppercase header/footer text: yes
    # Custom header/footer page number text: yes
    # Don't uppercase header/footer text and change page number text: yes
    # Swap reading header/footer: yes
    Enable advanced settings for all fonts: yes
    # Customize ComfortLight settings: yes
    # FeatureSettings - BookSpecificStats: yes
    # FeatureSettings - ShowFacebookShare: yes
    # FeatureSettings - FullScreenBrowser: yes
    # FeatureSettings - MyWords: yes
    # FeatureSettings - ExportHighlights: yes
    # DeveloperSettings - AutoUsbGadget: yes
    # PowerSettings - UnlockEnabled: yes
    Unify font sizes: yes
  src/librmsdk.so.1.0.0.yaml:
    # Disable orphans/widows avoidance: yes
    # Default ePub serif font (Amasis): yes
    # Default ePub sans-serif font (Gill Sans): yes
    # Default ePub symbol font (Symbol): yes
    # Force user line spacing in ePubs (Part 2 of 2): yes
    # Force user font-family in ePubs (Part 2 of 2): yes
    # Ignore ePub book Adobe XPGT stylesheet (page-template.xpgt): yes
    # Ignore ePub book CSS and Adobe XPGT stylesheets: yes
    # Ignore ePub TOC navpoints: yes
    # Default ePub monospace font: yes

## TRANSLATIONS ##
# Optional, use only if lrelease is not in PATH and if translations are needed
# lrelease: /path/to/lrelease

# Uncomment the following to add translations (replace lc with the language code)
# translations:
#   src/whatever.ts: usr/local/Kobo/translations/trans_lc.qm

## ADDITIONAL FILES ##
# Uncomment the following to add additional files to the tgz (like init scripts or hyphen dicts)
# The files will be root-owned, and world readable, writable, and executable (0777)
# files:
#   src/whatever.txt: usr/local/Kobo/whatever.txt
#   src/whateverToPutInMultiplePlaces.txt:
#     - usr/local/Kobo/location1.txt
#     - usr/local/Kobo/location2.txt

```

### 5、拼音输入法

在`.kobo/kobo/Kobo eReader.conf`文件的`[ApplicationPreferences]`下面添加一行`ExtraLocales=zh_CN`即可

### 6、禁止kobo原生系统扫描koreader等第三方插件中的七七八八的文件

依然是在`.kobo/kobo/Kobo eReader.conf`文件的末尾添加如下内容：

```
[FeatureSettings]
ExcludeSyncFolders=\\.(?!kobo|adobe).*?
```



## 结语：

点墨的kobo设备至此就配置完成了，在之后的使用过程中只需要简单的放入kepub书籍直接观看就好了

