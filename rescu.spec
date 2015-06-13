Name: rescu
Version: 1.7.2
Release: 1%{?dist}
Summary: Lightweight Rest client utility for Java

#Missing LICENSE file, upstream have been asked to provide one
License: MIT
URL: https://github.com/mmazi/rescu
Source0: https://github.com/mmazi/%{name}/archive/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: maven-local
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.slf4j:slf4j-api)

#Tests
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.testng:testng)
BuildRequires: mvn(com.google.guava:guava)
BuildRequires: mvn(org.hamcrest:hamcrest-all)
BuildRequires: mvn(joda-time:joda-time)
BuildRequires: mvn(org.mockito:mockito-all)

Requires: java-headless >= 1:1.6.0

%description
ResCU enables the user to create a proxy Rest client in run-time directly from a
JAX-RS annotated interface. ResCU is mostly focused on json-based services, and
uses Jackson for json-to-object mapping.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n rescu-rescu-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc README.md

%files javadoc -f .mfiles-javadoc
%doc README.md

%changelog
* Sat Jun 13 2015 Jonny Heggheim <hegjon@gmail.com> - 1.7.2-1
- Inital packaging
