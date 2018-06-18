project('freetype2', 'c',
  meson_version: '>= 0.47.0',
  version: '22.1.16',
  default_options: [ 'buildtype=debugoptimized'])

pkgmod = import('pkgconfig')

cc = meson.get_compiler('c')

base_sources = [
  'src/autofit/autofit.c',
  'src/base/ftbase.c',
  'src/base/ftbbox.c',
  'src/base/ftbdf.c',
  'src/base/ftbitmap.c',
  'src/base/ftcid.c',
  'src/base/ftfstype.c',
  'src/base/ftgasp.c',
  'src/base/ftglyph.c',
  'src/base/ftgxval.c',
  'src/base/ftinit.c',
  'src/base/ftmm.c',
  'src/base/ftotval.c',
  'src/base/ftpatent.c',
  'src/base/ftpfr.c',
  'src/base/ftstroke.c',
  'src/base/ftsynth.c',
  'src/base/ftsystem.c',
  'src/base/fttype1.c',
  'src/base/ftwinfnt.c',
  'src/bdf/bdf.c',
  'src/bzip2/ftbzip2.c',
  'src/cache/ftcache.c',
  'src/cff/cff.c',
  'src/cid/type1cid.c',
  'src/gzip/ftgzip.c',
  'src/lzw/ftlzw.c',
  'src/pcf/pcf.c',
  'src/pfr/pfr.c',
  'src/psaux/psaux.c',
  'src/pshinter/pshinter.c',
  'src/psnames/psnames.c',
  'src/raster/raster.c',
  'src/sfnt/sfnt.c',
  'src/smooth/smooth.c',
  'src/truetype/truetype.c',
  'src/type1/type1.c',
  'src/type42/type42.c',
  'src/winfonts/winfnt.c',
]

ft2build_h = [
  'include/ft2build.h',
]

ft_headers = [
  'include/freetype/freetype.h',
  'include/freetype/ftadvanc.h',
  'include/freetype/ftbbox.h',
  'include/freetype/ftbdf.h',
  'include/freetype/ftbitmap.h',
  'include/freetype/ftbzip2.h',
  'include/freetype/ftcache.h',
  'include/freetype/ftchapters.h',
  'include/freetype/ftcid.h',
  'include/freetype/ftdriver.h',
  'include/freetype/fterrdef.h',
  'include/freetype/fterrors.h',
  'include/freetype/ftfntfmt.h',
  'include/freetype/ftgasp.h',
  'include/freetype/ftglyph.h',
  'include/freetype/ftgxval.h',
  'include/freetype/ftgzip.h',
  'include/freetype/ftimage.h',
  'include/freetype/ftincrem.h',
  'include/freetype/ftlcdfil.h',
  'include/freetype/ftlist.h',
  'include/freetype/ftlzw.h',
  'include/freetype/ftmac.h',
  'include/freetype/ftmm.h',
  'include/freetype/ftmodapi.h',
  'include/freetype/ftmoderr.h',
  'include/freetype/ftotval.h',
  'include/freetype/ftoutln.h',
  'include/freetype/ftparams.h',
  'include/freetype/ftpfr.h',
  'include/freetype/ftrender.h',
  'include/freetype/ftsizes.h',
  'include/freetype/ftsnames.h',
  'include/freetype/ftstroke.h',
  'include/freetype/ftsynth.h',
  'include/freetype/ftsystem.h',
  'include/freetype/fttrigon.h',
  'include/freetype/fttypes.h',
  'include/freetype/ftwinfnt.h',
  'include/freetype/t1tables.h',
  'include/freetype/ttnameid.h',
  'include/freetype/tttables.h',
  'include/freetype/tttags.h',
]

ft_config_headers = [
  'include/freetype/config/ftmodule.h',
  'include/freetype/config/ftheader.h',
  'include/freetype/config/ftstdlib.h',
  'include/freetype/config/ftconfig.h',
]

if host_machine.system() == 'windows'
  winmod = import('windows')
  base_sources += [
    'builds/windows/ftdebug.c',
    winmod.compile_resources('src/base/ftver.rc'),
  ]
else
  base_sources += [
    'src/base/ftdebug.c',
  ]
endif

c_args = [
  '-DFT2_BUILD_LIBRARY',
  '-DFT_CONFIG_CONFIG_H=<ftconfig.h>',
  '-DFT_CONFIG_OPTIONS_H=<ftoption.h>'
]

if host_machine.system() == 'windows'
  c_args += [
    '-D_CRT_SECURE_NO_WARNINGS',
    '-D_CRT_NONSTDC_NO_WARNINGS',
  ]
endif

check_headers = []

if ['linux', 'darwin', 'cygwin'].contains(host_machine.system())
  check_headers += [
    ['unistd.h'],
    ['fcntl.h'],
    ['stdint.h'],
  ]
  ftconfig_h_in = files('builds/unix/ftconfig.h.in')
else
  ftconfig_h_in = files('include/freetype/config/ftconfig.h')
endif

check_optional_deps = [
  ['bzip2'],
  ['harfbuzz', {'version': '>= 1.3.0'}]
]

conf = configuration_data()
deps = []
incbase = include_directories(['include'])

foreach check : check_headers
  name = check[0]

  if cc.has_header(name)
    conf.set('HAVE_@0@'.format(name.to_upper().underscorify()), 1)
  endif
endforeach

foreach check : check_optional_deps
  name = check[0]
  opts = check.length() > 1 ? check[1] : {}
  pkg_name = opts.get('pkg', name)
  conf_name = 'FT_CONFIG_OPTION_USE_@0@'.format(name.to_upper())

  if opts.has_key('version')
    dep = dependency(pkg_name, version : opts['version'], required : false)
  else
    dep = dependency(pkg_name, required : false)
  endif

  conf.set(conf_name, dep.found())

  if dep.found()
    deps += [dep]
  endif
endforeach

zlib_dep = dependency('zlib', required: false, fallback: ['zlib', 'zlib_dep'])
if zlib_dep.found()
  conf.set('FT_CONFIG_OPTION_SYSTEM_ZLIB', 1)
  deps += [zlib_dep]
endif

png_dep = dependency('libpng',
  required: false,
  fallback: ['libpng', 'png_dep']
)
if png_dep.found()
  conf.set('FT_CONFIG_OPTION_USE_PNG', 1)
  deps += [png_dep]
endif

configure_file(input: ftconfig_h_in,
  output: 'ftconfig.h',
  configuration: conf)

ft_config_headers += [configure_file(input: 'include/freetype/config/ftoption.h.in',
  output: 'ftoption.h',
  configuration: conf)]

libfreetype = library('freetype', base_sources,
  include_directories: incbase,
  dependencies: deps,
  c_args: c_args,
  install: true,
  version: '6.16.0',
  soversion: '6')

freetype_dep = declare_dependency(link_with: libfreetype,
  include_directories : incbase,
  dependencies: deps
)

install_headers(ft2build_h, subdir: 'freetype2')
install_headers(ft_headers, subdir: 'freetype2/freetype')
install_headers(ft_config_headers, subdir: 'freetype2/freetype/config')

pkgmod.generate(libfreetype,
  name: 'freetype2',
  description: 'The FreeType font rendering library.',
  subdirs: ['freetype2'],
  version: meson.project_version())
