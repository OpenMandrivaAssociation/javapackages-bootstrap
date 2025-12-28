# Exclude automatically generated requires on java interpreter which is not
# owned by any package
%global __requires_exclude ^%{_jvmdir}/jre
# Generated list of bundled packages
%global _local_file_attrs local_generator
%global __local_generator_provides cat %{_builddir}/%{buildsubdir}/bundled-provides.txt
%global __local_generator_path ^%{metadataPath}/.*$
%global debug_package %{nil}
%global javaHomePath %(. %{_sysconfdir}/profile.d/90java.sh ; echo -n $JAVA_HOME)
%global mavenHomePath %{_datadir}/%{name}
%global metadataPath %{mavenHomePath}/maven-metadata
%global artifactsPath %{_datadir}
%global launchersPath %{_libexecdir}/%{name}

Name:           javapackages-bootstrap
Version:        1.27.0
Release:        1
Summary:        A means of bootstrapping Java Packages Tools
# For detailed info see the file javapackages-bootstrap-PACKAGE-LICENSING
License:        Apache-1.1 AND Apache-2.0 AND (Apache-2.0 OR EPL-2.0) AND (Apache-2.0 OR LGPL-2.0-or-later) AND BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND CPL-1.0 AND EPL-1.0 AND EPL-2.0 AND (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0) AND LicenseRef-Fedora-Public-Domain AND MIT AND Plexus AND SMLNJ AND Saxpath AND xpp
URL:            https://github.com/fedora-java/javapackages-bootstrap
BuildArch:      noarch

Source0:        https://github.com/fedora-java/javapackages-bootstrap/releases/download/%{version}/javapackages-bootstrap-%{version}.tar.zst
# License breakdown
Source1:        javapackages-bootstrap-PACKAGE-LICENSING
# To obtain the following sources:
# tar -xf ${name}-${version}.tar.zst
# pushd ${name}-${version}
# ./downstream.sh clone
# ./downstream.sh prep
# ./downstream.sh archive
# The results are in the archive directory
Source1001:     ant.tar.zst
Source1002:     aopalliance.tar.zst
Source1003:     apache-pom.tar.zst
Source1004:     apiguardian.tar.zst
Source1005:     asm.tar.zst
Source1006:     assertj-core.tar.zst
Source1007:     bnd.tar.zst
Source1008:     build-helper-maven-plugin.tar.zst
Source1009:     byte-buddy.tar.zst
Source1010:     cdi.tar.zst
Source1011:     chhorz-javadoc-parser.tar.zst
Source1012:     common-annotations-api.tar.zst
Source1013:     commons-beanutils.tar.zst
Source1014:     commons-cli.tar.zst
Source1015:     commons-codec.tar.zst
Source1016:     commons-collections.tar.zst
Source1017:     commons-compress.tar.zst
Source1018:     commons-io.tar.zst
Source1019:     commons-jxpath.tar.zst
Source1020:     commons-lang.tar.zst
Source1021:     commons-logging.tar.zst
Source1022:     commons-parent-pom.tar.zst
Source1023:     cup.tar.zst
Source1024:     disruptor.tar.zst
Source1025:     dola-gleaner.tar.zst
Source1026:     dola.tar.zst
Source1027:     dola-transformer.tar.zst
Source1028:     easymock.tar.zst
Source1029:     felix-parent-pom.tar.zst
Source1030:     felix-utils.tar.zst
Source1031:     fusesource-pom.tar.zst
Source1032:     gson.tar.zst
Source1033:     guava.tar.zst
Source1034:     guice.tar.zst
Source1035:     hamcrest.tar.zst
Source1036:     httpcomponents-client.tar.zst
Source1037:     httpcomponents-core.tar.zst
Source1038:     httpcomponents-parent-pom.tar.zst
Source1039:     injection-api.tar.zst
Source1040:     jaf-api.tar.zst
Source1041:     jansi.tar.zst
Source1042:     javacc-maven-plugin.tar.zst
Source1043:     javacc.tar.zst
Source1044:     javaparser.tar.zst
Source1045:     jcommander.tar.zst
Source1046:     jctools.tar.zst
Source1047:     jdom2.tar.zst
Source1048:     jdom.tar.zst
Source1049:     jflex.tar.zst
Source1050:     jline3.tar.zst
Source1051:     jsoup.tar.zst
Source1052:     jsr-305.tar.zst
Source1053:     junit4.tar.zst
Source1054:     junit5.tar.zst
Source1055:     kojan-parent.tar.zst
Source1056:     kojan-xml.tar.zst
Source1057:     log4j.tar.zst
Source1058:     mail-api.tar.zst
Source1059:     maven4.tar.zst
Source1060:     maven-antrun-plugin.tar.zst
Source1061:     maven-apache-resources.tar.zst
Source1062:     maven-archiver.tar.zst
Source1063:     maven-artifact-transfer.tar.zst
Source1064:     maven-assembly-plugin.tar.zst
Source1065:     maven-bundle-plugin.tar.zst
Source1066:     maven-common-artifact-filters.tar.zst
Source1067:     maven-compiler-plugin.tar.zst
Source1068:     maven-dependency-analyzer.tar.zst
Source1069:     maven-dependency-plugin.tar.zst
Source1070:     maven-dependency-tree.tar.zst
Source1071:     maven-file-management.tar.zst
Source1072:     maven-filtering.tar.zst
Source1073:     maven-jar-plugin.tar.zst
Source1074:     maven-parent-pom.tar.zst
Source1075:     maven-plugin-testing.tar.zst
Source1076:     maven-plugin-tools.tar.zst
Source1077:     maven.tar.zst
Source1078:     maven-remote-resources-plugin.tar.zst
Source1079:     maven-resolver2.tar.zst
Source1080:     maven-resolver.tar.zst
Source1081:     maven-resources-plugin.tar.zst
Source1082:     maven-shared-incremental.tar.zst
Source1083:     maven-shared-io.tar.zst
Source1084:     maven-shared-utils.tar.zst
Source1085:     maven-source-plugin.tar.zst
Source1086:     maven-surefire.tar.zst
Source1087:     maven-verifier.tar.zst
Source1088:     maven-wagon.tar.zst
Source1089:     mockito.tar.zst
Source1090:     modello.tar.zst
Source1091:     moditect.tar.zst
Source1092:     modulemaker-maven-plugin.tar.zst
Source1093:     mojo-parent-pom.tar.zst
Source1094:     objenesis.tar.zst
Source1095:     opentest4j.tar.zst
Source1096:     osgi-annotation.tar.zst
Source1097:     osgi-cmpn.tar.zst
Source1098:     osgi-core.tar.zst
Source1099:     picocli.tar.zst
Source1100:     plexus-archiver.tar.zst
Source1101:     plexus-build-api0.tar.zst
Source1102:     plexus-build-api.tar.zst
Source1103:     plexus-cipher.tar.zst
Source1104:     plexus-classworlds.tar.zst
Source1105:     plexus-compiler.tar.zst
Source1106:     plexus-containers.tar.zst
Source1107:     plexus-interactivity.tar.zst
Source1108:     plexus-interpolation.tar.zst
Source1109:     plexus-io.tar.zst
Source1110:     plexus-languages.tar.zst
Source1111:     plexus-pom.tar.zst
Source1112:     plexus-resources.tar.zst
Source1113:     plexus-sec-dispatcher4.tar.zst
Source1114:     plexus-sec-dispatcher.tar.zst
Source1115:     plexus-testing.tar.zst
Source1116:     plexus-utils4.tar.zst
Source1117:     plexus-utils.tar.zst
Source1118:     plexus-xml.tar.zst
Source1119:     qdox.tar.zst
Source1120:     servlet-api.tar.zst
Source1121:     sisu.tar.zst
Source1122:     slf4j2.tar.zst
Source1123:     slf4j.tar.zst
Source1124:     stax2-api.tar.zst
Source1125:     testng.tar.zst
Source1126:     univocity-parsers.tar.zst
Source1127:     velocity-engine.tar.zst
Source1128:     woodstox.tar.zst
Source1129:     xmlunit.tar.zst
Source1130:     xmvn.tar.zst
Source1131:     xz-java.tar.zst

BuildRequires:  byaccj
# For _javaconfdir macro
BuildRequires:  javapackages-filesystem
BuildRequires:  jdk-current
BuildRequires:  jurand
Requires:       bash
Requires:       coreutils
Requires:       jdk-current
Requires:       javapackages-common
Requires:       lujavrite
Requires:       procps-ng

%description
In a nutshell, Java Packages Bootstrap (JPB) is a standalone build of all Java
software packages that are required for Java Packages Tools (JPT) to work.

In order to achieve reliable and reproducible builds of Java packages while
meeting Fedora policy that requires everything to be built from source, without
using prebuilt binary artifacts, it is necessary to build the packages in a
well-defined, acyclic order. Dependency cycles between packages are the biggest
obstacle to achieving this goal and JPT is the biggest offender -- it requires
more than a hundred of Java packages, all of which in turn build-require JPT.

JPB comes with a solution to this problem -- it builds everything that JPT needs
to work, without reliance on any Java software other than OpenJDK. JPT can
depend on JPB for everything, without depending on any other Java packages. For
example, JPB contains embedded version of XMvn, removing dependency of JPT on
XMvn, allowing JPT to be used before one builds XMvn package.

%prep
%autosetup -p1 -C
mkdir archive/
cp %{sources} archive/
./downstream.sh prep-from-archive

%build
JAVA_HOME=%{javaHomePath} ./mbi.sh build -parallel

%install
JAVA_HOME=%{javaHomePath} ./mbi.sh dist \
  -javaCmdPath=%{javaHomePath}/bin/java \
  -basePackageName=%{name} \
  -installRoot=%{buildroot} \
  -mavenHomePath=%{mavenHomePath} \
  -metadataPath=%{metadataPath} \
  -artifactsPath=%{artifactsPath} \
  -launchersPath=%{launchersPath} \
  -licensesPath=%{_licensedir}/%{name} \

install -D -p -m 644 downstream/dola/dola-bsx/src/main/lua/dola-bsx.lua %{buildroot}%{_rpmluadir}/%{name}-dola-bsx.lua
install -D -p -m 644 downstream/dola/dola-dbs/src/main/lua/dola-dbs.lua %{buildroot}%{_rpmluadir}/%{name}-dola-dbs.lua
install -D -p -m 644 downstream/dola/dola-generator/src/main/lua/dola-generator.lua %{buildroot}%{_rpmluadir}/%{name}-dola-generator.lua
install -D -p -m 644 downstream/dola/dola-bsx/src/main/rpm/macros.dola-bsx %{buildroot}%{_rpmmacrodir}/macros.jpb-dola-bsx
install -D -p -m 644 downstream/dola/dola-dbs/src/main/rpm/macros.dola-dbs %{buildroot}%{_rpmmacrodir}/macros.zzz-jpb-dola-dbs
install -D -p -m 644 downstream/dola/dola-generator/src/main/rpm/macros.dola-generator %{buildroot}%{_rpmmacrodir}/macros.jpb-dola-generator
install -D -p -m 644 downstream/dola/dola-generator/src/main/rpm/macros.dola-generator-etc %{buildroot}%{_sysconfdir}/rpm/macros.jpb-dola-generator-etc
install -D -p -m 644 downstream/dola/dola-generator/src/main/rpm/dolagen.attr %{buildroot}%{_fileattrsdir}/jpbdolagen.attr
install -D -p -m 644 downstream/dola/dola-bsx/src/main/conf/dola-bsx.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/00-dola-bsx.conf
install -D -p -m 644 downstream/dola/dola-dbs/src/main/conf/dola-dbs.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/04-dola-dbs.conf
install -D -p -m 644 downstream/dola/dola-generator/src/main/conf/dola-generator.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/03-dola-generator.conf
install -D -p -m 644 downstream/dola/dola-bsx-api/src/main/conf/dola-bsx-api.conf %{buildroot}%{_javaconfdir}/%{name}/dola/classworlds/02-dola-bsx-api.conf

echo '
%%__xmvngen_debug 1
%%__xmvngen_libjvm %{javaHomePath}/lib/server/libjvm.so
%%__xmvngen_classpath %{artifactsPath}/%{name}/xmvn-generator.jar:%{artifactsPath}/%{name}/asm.jar:%{artifactsPath}/%{name}/commons-compress.jar:%{artifactsPath}/%{name}/commons-io.jar:%{artifactsPath}/%{name}/xmvn-mojo.jar:%{artifactsPath}/%{name}/kojan-xml.jar:%{artifactsPath}/%{name}/maven-model.jar:%{artifactsPath}/%{name}/plexus-utils.jar
%%__xmvngen_provides_generators org.fedoraproject.xmvn.generator.filesystem.FilesystemGeneratorFactory org.fedoraproject.xmvn.generator.jpscript.JPackageScriptGeneratorFactory org.fedoraproject.xmvn.generator.jpms.JPMSGeneratorFactory org.fedoraproject.xmvn.generator.maven.MavenGeneratorFactory
%%__xmvngen_requires_generators org.fedoraproject.xmvn.generator.filesystem.FilesystemGeneratorFactory org.fedoraproject.xmvn.generator.jpscript.JPackageScriptGeneratorFactory org.fedoraproject.xmvn.generator.maven.MavenGeneratorFactory
%%__xmvngen_post_install_hooks org.fedoraproject.xmvn.generator.transformer.TransformerHookFactory
%%jpb_env PATH=/usr/libexec/javapackages-bootstrap:%{javaHomePath}/bin:$PATH
%%java_home %{javaHomePath}
' >%{buildroot}%{_rpmmacrodir}/macros.jpbgen

# Dynamically generate bundled Provides
./downstream.sh bundled-provides >bundled-provides.txt

%check
%{buildroot}%{launchersPath}/xmvn --version

%files
%{mavenHomePath}
%{launchersPath}/*
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*
%{_javaconfdir}/%{name}

%license %{_licensedir}/%{name}
%doc README.md
%doc AUTHORS
