TUNE=base
LABEL=mytest-m64
NUMBER=657
NAME=xz_s
SOURCES= spec.c spec_xz.c pxz.c common/tuklib_physmem.c \
	 liblzma/common/common.c liblzma/common/block_util.c \
	 liblzma/common/easy_preset.c liblzma/common/filter_common.c \
	 liblzma/common/hardware_physmem.c liblzma/common/index.c \
	 liblzma/common/stream_flags_common.c liblzma/common/vli_size.c \
	 liblzma/common/alone_encoder.c liblzma/common/block_buffer_encoder.c \
	 liblzma/common/block_encoder.c liblzma/common/block_header_encoder.c \
	 liblzma/common/easy_buffer_encoder.c liblzma/common/easy_encoder.c \
	 liblzma/common/easy_encoder_memusage.c \
	 liblzma/common/filter_buffer_encoder.c liblzma/common/filter_encoder.c \
	 liblzma/common/filter_flags_encoder.c liblzma/common/index_encoder.c \
	 liblzma/common/stream_buffer_encoder.c liblzma/common/stream_encoder.c \
	 liblzma/common/stream_flags_encoder.c liblzma/common/vli_encoder.c \
	 liblzma/common/alone_decoder.c liblzma/common/auto_decoder.c \
	 liblzma/common/block_buffer_decoder.c liblzma/common/block_decoder.c \
	 liblzma/common/block_header_decoder.c \
	 liblzma/common/easy_decoder_memusage.c \
	 liblzma/common/filter_buffer_decoder.c liblzma/common/filter_decoder.c \
	 liblzma/common/filter_flags_decoder.c liblzma/common/index_decoder.c \
	 liblzma/common/index_hash.c liblzma/common/stream_buffer_decoder.c \
	 liblzma/common/stream_decoder.c liblzma/common/stream_flags_decoder.c \
	 liblzma/common/vli_decoder.c liblzma/check/check.c \
	 liblzma/check/crc32_table.c liblzma/check/crc32_fast.c \
	 liblzma/check/crc64_table.c liblzma/check/crc64_fast.c \
	 liblzma/check/sha256.c liblzma/lz/lz_encoder.c \
	 liblzma/lz/lz_encoder_mf.c liblzma/lz/lz_decoder.c \
	 liblzma/lzma/lzma_encoder.c liblzma/lzma/lzma_encoder_presets.c \
	 liblzma/lzma/lzma_encoder_optimum_fast.c \
	 liblzma/lzma/lzma_encoder_optimum_normal.c liblzma/lzma/fastpos_table.c \
	 liblzma/lzma/lzma_decoder.c liblzma/lzma/lzma2_encoder.c \
	 liblzma/lzma/lzma2_decoder.c liblzma/rangecoder/price_table.c \
	 liblzma/delta/delta_common.c liblzma/delta/delta_encoder.c \
	 liblzma/delta/delta_decoder.c liblzma/simple/simple_coder.c \
	 liblzma/simple/simple_encoder.c liblzma/simple/simple_decoder.c \
	 liblzma/simple/x86.c liblzma/simple/powerpc.c liblzma/simple/ia64.c \
	 liblzma/simple/arm.c liblzma/simple/armthumb.c liblzma/simple/sparc.c \
	 xz/args.c xz/coder.c xz/file_io.c xz/hardware.c xz/list.c xz/main.c \
	 xz/message.c xz/options.c xz/signals.c xz/util.c \
	 common/tuklib_open_stdxxx.c common/tuklib_progname.c \
	 common/tuklib_exit.c common/tuklib_cpucores.c \
	 common/tuklib_mbstr_width.c common/tuklib_mbstr_fw.c \
	 spec_mem_io/spec_mem_io.c sha-2/sha512.c
EXEBASE=xz_s
NEED_MATH=
BENCHLANG=C

BENCH_FLAGS      = -DSPEC_AUTO_BYTEORDER=0x12345678 -DHAVE_CONFIG_H=1 -DSPEC_MEM_IO -DSPEC_XZ -I. -Ispec_mem_io -Isha-2 -Icommon -Iliblzma/api -Iliblzma/lzma -Iliblzma/common -Iliblzma/check -Iliblzma/simple -Iliblzma/delta -Iliblzma/lz -Iliblzma/rangecoder
CC               = $(SPECLANG)gcc     -std=c99   -m64
CC_VERSION_OPTION = -v
CXX              = $(SPECLANG)g++     -std=c++03 -m64
CXX_VERSION_OPTION = -v
EXTRA_COPTIMIZE  = -fno-strict-aliasing -fgnu89-inline
EXTRA_OPTIMIZE   = -fopenmp -DSPEC_OPENMP
EXTRA_PORTABILITY = -DSPEC_LP64
FC               = $(SPECLANG)gfortran           -m64
FC_VERSION_OPTION = -v
OPTIMIZE         = -g
OS               = unix
SPECLANG         = /usr/bin/
absolutely_no_locking = 0
abstol           = 
action           = build
allow_label_override = 0
backup_config    = 1
baseexe          = xz_s
basepeak         = 0
benchdir         = benchspec
benchmark        = 657.xz_s
binary           = 
bindir           = exe
builddir         = build
bundleaction     = 
bundlename       = 
calctol          = 0
changedhash      = 0
check_version    = 0
clean_between_builds = no
command_add_redirect = 1
commanderrfile   = speccmds.err
commandexe       = xz_s_base.mytest-m64
commandfile      = speccmds.cmd
commandoutfile   = speccmds.out
commandstdoutfile = speccmds.stdout
comparedir       = compare
compareerrfile   = compare.err
comparefile      = compare.cmd
compareoutfile   = compare.out
comparestdoutfile = compare.stdout
compile_error    = 0
compwhite        = 
configdir        = config
configfile       = my-gcc-linux-x86.cfg
configpath       = /scratch/wayedt/spec2017_root/config/my-gcc-linux-x86.cfg
copies           = 1
current_range    = 
datadir          = data
default_size     = ref
default_submit   = $command
delay            = 0
deletebinaries   = 0
deletework       = 0
dependent_workloads = 0
device           = 
difflines        = 10
dirprot          = 511
discard_power_samples = 0
enable_monitor   = 1
endian           = 12345678
env_vars         = 0
expand_notes     = 0
expid            = 
exthash_bits     = 256
failflags        = 0
fake             = 1
feedback         = 1
flag_url_base    = https://www.spec.org/auto/cpu2017/Docs/benchmarks/flags/
floatcompare     = 
force_monitor    = 0
from_runcpu      = 2
fw_bios          = American Megatrends 39030100 02/29/2016
hostname         = login1.ittc.ku.edu
http_proxy       = 
http_timeout     = 30
hw_avail         = Nov-2021
hw_cpu_max_mhz   = 2999
hw_cpu_name      = Intel Xeon E5450
hw_cpu_nominal_mhz = 3999
hw_disk          = 50 TB  add more disk info here
hw_memory001     = 15.513 GB fixme: If using DDR4, the format is:
hw_memory002     = 'N GB (N x N GB nRxn PC4-nnnnX-X)'
hw_model         = TurboBlaster 3000
hw_nchips        = 2
hw_ncores        = 4
hw_ncpuorder     = 4 chips
hw_nthreadspercore = 4
hw_ocache        = None
hw_other         = None
hw_pcache        = 50 KB I + 50 KB D on chip per core
hw_scache        = None
hw_tcache        = None
hw_vendor        = Intel
idle_current_range = 
idledelay        = 10
idleduration     = 60
ignore_errors    = 1
ignore_sigint    = 0
ignorecase       = 
info_wrap_columns = 50
inputdir         = input
inputgenerrfile  = inputgen.err
inputgenfile     = inputgen.cmd
inputgenoutfile  = inputgen.out
inputgenstdoutfile = inputgen.stdout
iteration        = -1
iterations       = 1
keeptmp          = 0
label            = mytest-m64
license_num      = nnn (Your SPEC license number)
line_width       = 1020
link_input_files = 1
locking          = 1
log              = CPU2017
log_line_width   = 1020
log_timestamp    = 0
logfile          = /scratch/wayedt/spec2017_root/tmp/CPU2017.033/templogs/preenv.intspeed.033.0
logname          = /scratch/wayedt/spec2017_root/tmp/CPU2017.033/templogs/preenv.intspeed.033.0
lognum           = 033.0
mail_reports     = all
mailcompress     = 0
mailmethod       = smtp
mailport         = 25
mailserver       = 127.0.0.1
mailto           = 
make             = specmake
make_no_clobber  = 0
makefile_template = Makefile.YYYtArGeTYYYspec
makeflags        = --jobs=2
max_average_uncertainty = 1
max_hum_limit    = 0
max_report_runs  = 3
max_unknown_uncertainty = 1
mean_anyway      = 1
meter_connect_timeout = 30
meter_errors_default = 5
meter_errors_percentage = 5
min_report_runs  = 2
min_temp_limit   = 20
minimize_builddirs = 0
minimize_rundirs = 0
name             = xz_s
nansupport       = 
need_math        = 
no_input_handler = close
no_monitor       = 
noratios         = 0
note_preenv      = 1
notes_plat_sysinfo_000 =  Sysinfo program /scratch/wayedt/spec2017_root/bin/sysinfo
notes_plat_sysinfo_005 =  Rev: r5974 of 2018-05-19 9bcde8f2999c33d61f64985e45859ea9
notes_plat_sysinfo_010 =  running on login1.ittc.ku.edu Fri Nov 26 21:54:06 2021
notes_plat_sysinfo_015 = 
notes_plat_sysinfo_020 =  SUT (System Under Test) info as seen by some common utilities.
notes_plat_sysinfo_025 =  For more information on this section, see
notes_plat_sysinfo_030 =     https://www.spec.org/cpu2017/Docs/config.html\#sysinfo
notes_plat_sysinfo_035 = 
notes_plat_sysinfo_040 =  From /proc/cpuinfo
notes_plat_sysinfo_045 =     model name : Intel(R) Xeon(R) CPU E5450 @ 3.00GHz
notes_plat_sysinfo_050 =        2  "physical id"s (chips)
notes_plat_sysinfo_055 =        8 "processors"
notes_plat_sysinfo_060 =     cores, siblings (Caution: counting these is hw and system dependent. The following
notes_plat_sysinfo_065 =     excerpts from /proc/cpuinfo might not be reliable.  Use with caution.)
notes_plat_sysinfo_070 =        cpu cores : 4
notes_plat_sysinfo_075 =        siblings  : 4
notes_plat_sysinfo_080 =        physical 0: cores 0 1 2 3
notes_plat_sysinfo_085 =        physical 1: cores 0 1 2 3
notes_plat_sysinfo_090 = 
notes_plat_sysinfo_095 =  From lscpu:
notes_plat_sysinfo_100 =       Architecture:          x86_64
notes_plat_sysinfo_105 =       CPU op-mode(s):        32-bit, 64-bit
notes_plat_sysinfo_110 =       Byte Order:            Little Endian
notes_plat_sysinfo_115 =       CPU(s):                8
notes_plat_sysinfo_120 =       On-line CPU(s) list:   0-7
notes_plat_sysinfo_125 =       Thread(s) per core:    1
notes_plat_sysinfo_130 =       Core(s) per socket:    4
notes_plat_sysinfo_135 =       Socket(s):             2
notes_plat_sysinfo_140 =       NUMA node(s):          1
notes_plat_sysinfo_145 =       Vendor ID:             GenuineIntel
notes_plat_sysinfo_150 =       CPU family:            6
notes_plat_sysinfo_155 =       Model:                 23
notes_plat_sysinfo_160 =       Model name:            Intel(R) Xeon(R) CPU           E5450  @ 3.00GHz
notes_plat_sysinfo_165 =       Stepping:              6
notes_plat_sysinfo_170 =       CPU MHz:               2992.683
notes_plat_sysinfo_175 =       BogoMIPS:              5985.03
notes_plat_sysinfo_180 =       Virtualization:        VT-x
notes_plat_sysinfo_185 =       L1d cache:             32K
notes_plat_sysinfo_190 =       L1i cache:             32K
notes_plat_sysinfo_195 =       L2 cache:              6144K
notes_plat_sysinfo_200 =       NUMA node0 CPU(s):     0-7
notes_plat_sysinfo_205 = 
notes_plat_sysinfo_210 =  /proc/cpuinfo cache data
notes_plat_sysinfo_215 =     cache size : 6144 KB
notes_plat_sysinfo_220 = 
notes_plat_sysinfo_225 =  From numactl --hardware  WARNING: a numactl 'node' might or might not correspond to a
notes_plat_sysinfo_230 =  physical chip.
notes_plat_sysinfo_235 = 
notes_plat_sysinfo_240 =  From /proc/meminfo
notes_plat_sysinfo_245 =     MemTotal:       16266508 kB
notes_plat_sysinfo_250 =     HugePages_Total:       0
notes_plat_sysinfo_255 =     Hugepagesize:       2048 kB
notes_plat_sysinfo_260 = 
notes_plat_sysinfo_265 =  /usr/bin/lsb_release -d
notes_plat_sysinfo_270 =     CentOS Linux release 7.2.1511 (Core)
notes_plat_sysinfo_275 = 
notes_plat_sysinfo_280 =  From /etc/*release* /etc/*version*
notes_plat_sysinfo_285 =     centos-release: CentOS Linux release 7.2.1511 (Core)
notes_plat_sysinfo_290 =     centos-release-upstream: Derived from Red Hat Enterprise Linux 7.2 (Source)
notes_plat_sysinfo_295 =     os-release:
notes_plat_sysinfo_300 =        NAME="CentOS Linux"
notes_plat_sysinfo_305 =        VERSION="7 (Core)"
notes_plat_sysinfo_310 =        ID="centos"
notes_plat_sysinfo_315 =        ID_LIKE="rhel fedora"
notes_plat_sysinfo_320 =        VERSION_ID="7"
notes_plat_sysinfo_325 =        PRETTY_NAME="CentOS Linux 7 (Core)"
notes_plat_sysinfo_330 =        ANSI_COLOR="0;31"
notes_plat_sysinfo_335 =        CPE_NAME="cpe:/o:centos:centos:7"
notes_plat_sysinfo_340 =     redhat-release: CentOS Linux release 7.2.1511 (Core)
notes_plat_sysinfo_345 =     system-release: CentOS Linux release 7.2.1511 (Core)
notes_plat_sysinfo_350 =     system-release-cpe: cpe:/o:centos:centos:7
notes_plat_sysinfo_355 = 
notes_plat_sysinfo_360 =  uname -a:
notes_plat_sysinfo_365 =     Linux login1.ittc.ku.edu 3.10.0-514.el7.x86_64 \#1 SMP Tue Nov 22 16:42:41 UTC 2016
notes_plat_sysinfo_370 =     x86_64 x86_64 x86_64 GNU/Linux
notes_plat_sysinfo_375 = 
notes_plat_sysinfo_380 =  run-level 3 Sep 13 09:03
notes_plat_sysinfo_385 = 
notes_plat_sysinfo_390 =  SPEC is set to: /scratch/wayedt/spec2017_root
notes_plat_sysinfo_395 =     Filesystem               Type   Size  Used Avail Use% Mounted on
notes_plat_sysinfo_400 =     panfs://pfs.local:global panfs   50T   18T   33T  35% /panfs
notes_plat_sysinfo_405 = 
notes_plat_sysinfo_410 =  Cannot run dmidecode; consider saying 'chmod +s /usr/sbin/dmidecode'
notes_plat_sysinfo_415 = 
notes_plat_sysinfo_420 =  (End of data from sysinfo program)
notes_wrap_columns = 0
notes_wrap_indent =   
num              = 657
obiwan           = 
os_exe_ext       = 
output_format    = txt,html,cfg,pdf,csv
output_root      = 
outputdir        = output
parallel_test    = 0
parallel_test_submit = 0
parallel_test_workloads = 
path             = /scratch/wayedt/spec2017_root/benchspec/CPU/657.xz_s
plain_train      = 1
platform         = 
power            = 0
preENV_LD_LIBRARY_PATH = %{gcc_dir}/lib64/:%{gcc_dir}/lib/:/lib64
preenv           = 0
prefix           = 
prepared_by      = s181p983  (is never output, only tags rawfile)
ranks            = 1
rawhash_bits     = 256
rebuild          = 1
reftime          = reftime
reltol           = 
reportable       = 0
resultdir        = result
review           = 0
run              = all
runcpu           = /scratch/wayedt/spec2017_root/bin/harness/runcpu --configfile my-gcc-linux-x86.cfg --fake --action build --noreportable --nopower --runmode speed --tune base --size refspeed 657.xz_s --nopreenv --note-preenv --logfile /scratch/wayedt/spec2017_root/tmp/CPU2017.033/templogs/preenv.intspeed.033.0 --lognum 033.0 --from_runcpu 2
rundir           = run
runmode          = speed
safe_eval        = 1
save_build_files = 
section_specifier_fatal = 1
setprocgroup     = 1
setup_error      = 0
sigint           = 2
size             = refspeed
size_class       = ref
skipabstol       = 
skipobiwan       = 
skipreltol       = 
skiptol          = 
smarttune        = base
specdiff         = specdiff
specrun          = specinvoke
srcalt           = 
srcdir           = src
srcsource        = /scratch/wayedt/spec2017_root/benchspec/CPU/557.xz_r/src
stagger          = 10
strict_rundir_verify = 1
sw_avail         = Nov-2021
sw_base_ptrsize  = 64-bit
sw_compiler001   = C/C++/Fortran: Version 7.2.1 of GCC, the
sw_compiler002   = GNU Compiler Collection
sw_file          = panfs
sw_os001         = CentOS Linux release 7.2.1511 (Core)
sw_os002         = 3.10.0-514.el7.x86_64
sw_other         = None
sw_peak_ptrsize  = 64-bit
sw_state         = Run level 3 (add definition here)
sysinfo_hash_bits = 256
sysinfo_program  = specperl /scratch/wayedt/spec2017_root/bin/sysinfo
sysinfo_program_hash = sysinfo:SHA:32259ebd59f3e93740723202f27c44c82ee68e0f2e40cd2ca50cfd5519772397
table            = 1
teeout           = 1
test_date        = Nov-2021
test_sponsor     = My Corporation
tester           = My Corporation
threads          = 4
top              = /scratch/wayedt/spec2017_root
train_single_thread = 0
train_with       = train
tune             = base
uid              = 100589214
unbuffer         = 1
uncertainty_exception = 5
update           = 0
update_url       = http://www.spec.org/auto/cpu2017/updates/
use_submit_for_compare = 0
use_submit_for_speed = 0
username         = s181p983
verbose          = 5
verify_binaries  = 1
version          = 0.906000
version_url      = http://www.spec.org/auto/cpu2017/current_version
voltage_range    = 
worklist         = list
OUTPUT_RMFILES   = IMG_2560.cr2-40-4.out input.combined-40-8.out
