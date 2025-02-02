{
	"targets": [{
		"target_name": "spdlog",
		"sources": [
			"src/main.cc",
			"src/logger.cc"
		],
		"include_dirs": [
			"<!(node -e \"require('nan')\")",
			"deps/spdlog/include"
		],
		'cflags!': ['-fno-exceptions'],
		'cflags_cc!': ['-fno-exceptions'],
		'msvs_settings': {
			'VCCLCompilerTool': {
				'AdditionalOptions': [
					'/Qspectre',
					'/guard:cf'
				]
			},
			'VCLinkerTool': {
				'AdditionalOptions': [
					'/guard:cf'
				]
			}
		},
		'conditions': [
			['OS=="mac"', {
				'xcode_settings': {
					'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
				}
			}],
			['OS=="win"', {
				'defines': [
					'SPDLOG_WCHAR_FILENAMES'
				]
			}]
		]
	}]
}
