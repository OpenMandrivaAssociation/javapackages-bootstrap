#!/bin/sh
set -eu

normalize_version() {
    v="$1"

    # If it contains a hyphen, split into base + qualifier
    if echo "$v" | grep -q '-'; then
        base="${v%%-*}"
        rest="${v#*-}"

        # Remove remaining hyphens inside qualifier
        rest="${rest//-/}"

        # OpenMandriva style: base-0.qualifier.1
        echo "${base}-0.${rest}.1"
    else
        # No qualifier, version is fine
        echo "$v"
    fi
}

for f in project/*.properties; do
    b=${f##*/}
    p=${b%%.properties}
    echo "$p $f"
done | sed -n '
s/^commons-beanutils /apache-commons-beanutils /
s/^commons-cli /apache-commons-cli /
s/^commons-codec /apache-commons-codec /
s/^commons-collections /apache-commons-collections /
s/^commons-compress /apache-commons-compress /
s/^commons-io /apache-commons-io /
s/^commons-jxpath /apache-commons-jxpath /
s/^commons-lang /apache-commons-lang3 /
s/^commons-logging /apache-commons-logging /
s/^commons-parent-pom /apache-commons-parent /
s/^apache-pom /apache-parent /
s/^bnd /aqute-bnd /
s/^injection-api /atinject /
s/^jaf-api /jakarta-activation1 /
s/^jcommander /beust-jcommander /
s/^cdi /cdi-api /
s/^felix-parent-pom /felix-parent /
s/^guice /google-guice /
s/^httpcomponents-parent-pom /httpcomponents-project /
s/^common-annotations-api /jakarta-annotations /
s/^servlet-api /jakarta-servlet /
s/^cup /java_cup /
s/^junit4 /junit /
s/^mail-api /jakarta-mail /
s/^maven-parent-pom /maven-parent /
s/^maven-bundle-plugin /maven-plugin-bundle /
s/^mojo-parent-pom /mojo-parent /
s/^asm /objectweb-asm /
s/^osgi-cmpn /osgi-compendium /
s/^sisu-inject /sisu /
s/^oss-parent-pom /sonatype-oss-parent /
s/^velocity-engine /velocity /
p
' | while read fp mp; do
    . $mp
    norm=$(normalize_version "$version")
    echo "bundled($fp) = $norm"
done
