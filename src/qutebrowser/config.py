config.load_autoconfig(False)

config.set('content.cookies.accept', 'all', 'chrome-devtools://*')

config = config  # type: ConfigAPI # noqa: F821 pylint: disable=E0602,C0103
c = c  # type: ConfigContainer # noqa: F821 pylint: disable=E0602,C0103

#dark theme
c.colors.webpage.darkmode.algorithm = 'lightness-cielab'
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.threshold.text = 150
c.colors.webpage.darkmode.threshold.background = 205
c.colors.webpage.darkmode.policy.images = 'smart'

# disable insert mode completely
c.input.insert_mode.auto_enter = False
c.input.insert_mode.auto_leave = False
c.input.insert_mode.plugins = False

# Forward unbound keys
c.input.forward_unbound_keys = "all"


#emacs stuff from now on

ESC_BIND = 'clear-keychain ;; search ;; fullscreen --leave'

c.bindings.default['normal'] = {}
# Bindings
c.bindings.commands['normal'] = {
	# Navigation
	'<ctrl-v>': 'scroll-page 0 0.5',
	'<alt-v>': 'scroll-page 0 -0.5',
	'<ctrl-shift-v>': 'scroll-page 0 1',
	'<alt-shift-v>': 'scroll-page 0 -1',
	# FIXME come up with logical bindings for scrolling left/right

	# Commands
	'<alt-x>': 'set-cmd-text :',
	'<ctrl-x>bl': 'bookmark-list',
        '<ctrl-x>ba': 'bookmark-add',
        '<ctrl-x>bd': 'bookmark-del',
	'<ctrl-x>k': 'tab-close',
	'<ctrl-x><ctrl-c>': 'quit',
        '<ctrl-x>r': 'reload',


	'<ctrl-s>': 'set-cmd-text /',
	'<ctrl-r>': 'set-cmd-text ?',

	# hinting
	'<alt-s>': 'hint all',

	# history
	# FIXME maybe this should be <C-b> <C-n>? Or would that be too confusing?
	'<ctrl-]>': 'forward',
	'<ctrl-[>': 'back',

	# tabs
	'<ctrl-tab>': 'tab-next',
        '<ctrl-x>o': 'tab-next',
	'<ctrl-shift-tab>': 'tab-prev',

	# open links
	'<ctrl-l>': 'set-cmd-text -s :open',
	'<alt-l>': 'set-cmd-text -s :open -t',

	# editing
	'<ctrl-f>': 'fake-key <Right>',
	'<ctrl-b>': 'fake-key <Left>',
	'<ctrl-a>': 'fake-key <Home>',
	'<ctrl-e>': 'fake-key <End>',
	'<ctrl-n>': 'fake-key <Down>',
	'<ctrl-p>': 'fake-key <Up>',
	'<alt-f>': 'fake-key <Ctrl-Right>',
	'<alt-b>': 'fake-key <Ctrl-Left>',
	'<ctrl-d>': 'fake-key <Delete>',
	'<alt-d>': 'fake-key <Ctrl-Delete>',
	'<alt-backspace>': 'fake-key <Ctrl-Backspace>',
	'<ctrl-w>': 'fake-key <Ctrl-backspace>',
	'<ctrl-y>': 'insert-text {primary}',

	# Numbers
	# https://github.com/qutebrowser/qutebrowser/issues/4213
	'1': 'fake-key 1',
	'2': 'fake-key 2',
	'3': 'fake-key 3',
	'4': 'fake-key 4',
	'5': 'fake-key 5',
	'6': 'fake-key 6',
	'7': 'fake-key 7',
	'8': 'fake-key 8',
	'9': 'fake-key 9',
	'0': 'fake-key 0',

	# escape hatch
	'<ctrl-h>': 'set-cmd-text -s :help',
	'<ctrl-g>': ESC_BIND,
}

c.bindings.commands['command'] = {
	'<ctrl-s>': 'search-next',
	'<ctrl-r>': 'search-prev',

	'<ctrl-p>': 'completion-item-focus prev',
	'<ctrl-n>': 'completion-item-focus next',

	'<alt-p>': 'command-history-prev',
	'<alt-n>': 'command-history-next',

	# escape hatch
	'<ctrl-g>': 'mode-leave',
}

c.bindings.commands['hint'] = {
	# escape hatch
	'<ctrl-g>': 'mode-leave',
}


c.bindings.commands['caret'] = {
	# escape hatch
	'<ctrl-g>': 'mode-leave',
}
