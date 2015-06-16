#Not released yet
%define revision 1dfa94b3bd68dff9033813234fbf948179fe6f17
#Missing some test dependencies
%define _without_tests 1

Name: rescu
Version: 1.8.2
Release: 0%{?dist}
Summary: Lightweight Rest client utility for Java

License: MIT
URL: https://github.com/mmazi/rescu
Source0: https://github.com/mmazi/%{name}/archive/%{revision}.tar.gz
Source1: rescu-LICENSE
BuildArch: noarch

BuildRequires: maven-local
BuildRequires: mvn(javax.ws.rs:jsr311-api)
BuildRequires: mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(net.iharder:base64)

%description
ResCU enables the user to create a proxy Rest client in run-time directly from a
JAX-RS annotated interface. ResCU is mostly focused on json-based services, and
uses Jackson for json-to-object mapping.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n rescu-%{revision}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc README.md
%license LICENSE.txt

%changelog
* Tue Jun 16 2015 Jonny Heggheim <hegjon@gmail.com> - 1.8.2-0
- Inital packaging
