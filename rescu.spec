#Not released yet
%define revision 1dfa94b3bd68dff9033813234fbf948179fe6f17

Name: rescu
Version: 1.8.2
Release: 0.1%{?dist}
Summary: Lightweight Rest client utility for Java

License: MIT
URL: https://github.com/mmazi/rescu
Source0: https://github.com/mmazi/%{name}/archive/%{revision}.tar.gz
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
# Skip tests for now, missing dependencies:
# org.assertj:assertj-core:2.1.0
# eu.codearte.catch-exception:catch-exception:1.4.4
# org.hamcrest:hamcrest-junit:2.0.0.0
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc README.md
%license LICENSE.txt

%changelog
* Tue Jun 16 2015 Jonny Heggheim <hegjon@gmail.com> - 1.8.2-0.1
- Inital packaging
