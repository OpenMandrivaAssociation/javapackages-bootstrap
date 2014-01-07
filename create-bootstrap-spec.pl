#!/usr/bin/perl

if ($#ARGV < 0) {
    die("usage: create-bootstrap-spec.pl source-rpm\n");
}
my $rpm = $ARGV[0];
shift(@ARGV);

print("
%undefine _compress
%undefine _extension
%global _duplicate_files_terminate_build 0
%global _files_listed_twice_terminate_build 0
%global _unpackaged_files_terminate_build 0
%global _nonzero_exit_pkgcheck_terminate_build 0
%global _use_internal_dependency_generator 0
%global __find_requires /bin/sed -e 's/.*//'
%global __find_provides /bin/sed -e 's/.*//'
");
my $str = `rpm -qp --qf "%{EPOCH} %{NAME} %{VERSION} %{RELEASE}" $rpm`;
my ($epoch, $name, $version, $release) = split(/ /, $str);
print("
Name:		$name");
if ($epoch != "(none)") {
    print("
Epoch:		$epoch");
}
print("
Version:	$version
Release:	$release
License:	GPLv3+
Source0:	$rpm
");
my $index = 1;
foreach my $extra (@ARGV) {
    print("Source$index:	$extra\n");
    ++$index;
}
print("
URL:		https://abf.rosalinux.ru/openmandriva/$name
BuildArch:	noarch
Summary:	$name bootstrap version
Requires:	javapackages-bootstrap
");
my $req = `rpm -qp --requires $rpm | egrep -v '(rpmlib)' | sort -u`;
foreach (split('\n', $req)) {
    print("Requires:	$_\n");
}
my $prv = `rpm -qp --provides $rpm | egrep -v '(rpmlib)' | sort -u`;
foreach (split('\n', $prv)) {
    print("Provides:	$_\n");
}
my $obs = `rpm -qp --obsoletes $rpm | egrep -v '(rpmlib)' | sort -u`;
foreach (split('\n', $obs)) {
    print("Obsoletes:	$_\n");
}
print("
%description
$name bootstrap version.

%files
");
my $list=`LC_ALL=C rpm -qpl $rpm`;
$list =~ s/\(contains no files\)//;
$list =~ s/([\(\[\{ \}\]\)])/?/g;
print("$list");

foreach my $extra (@ARGV) {
    my $str = `rpm -qp --qf "%{EPOCH} %{NAME} %{VERSION} %{RELEASE}" $extra`;
    my ($epoch, $name, $version, $release) = split(/ /, $str);
    print("
#------------------------------------------------------------------------
%package	-n $name");
    if ($epoch != "(none)") {
    print("
Epoch:		$epoch");
    }
    print("
Version:	$version
Release:	$release
Summary:	$name bootstrap version
Requires:	javapackages-bootstrap
");
    my $req = `rpm -qp --requires $extra | egrep -v '(rpmlib)' | sort -u`;
    foreach (split('\n', $req)) {
	print("Requires:	$_\n");
    }
    my $prv = `rpm -qp --provides $extra | egrep -v '(rpmlib)' | sort -u`;
    foreach (split('\n', $prv)) {
	print("Provides:	$_\n");
    }
    my $obs = `rpm -qp --obsoletes $extra | egrep -v '(rpmlib)' | sort -u`;
    foreach (split('\n', $obs)) {
	print("Obsoletes:	$_\n");
    }
print("
%description	-n $name
$name bootstrap version.

%files		-n $name
");
    my $list=`LC_ALL=C rpm -qpl $extra`;
    $list =~ s/\(contains no files\)//;
    $list =~ s/([\(\[\{ \}\]\)])/?/g;
    print("$list");
}

print("
#------------------------------------------------------------------------
%prep

%build

%install
cd %{buildroot}
rpm2cpio %{SOURCE0} | cpio -id\n");
$index = 1;
foreach my $extra (@ARGV) {
    print("rpm2cpio %{SOURCE$index} | cpio -id\n");
    ++$index;
}
