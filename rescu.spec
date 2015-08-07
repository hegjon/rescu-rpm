#Not released yet
%global revision 35ef764e51005ce0d31dc90c0bd9227f6082fb01
%global short_sha 35ef764

Name: rescu
Version: 1.8.2
Release: 0.1.git%{short_sha}%{?dist}
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
* Fri Aug 07 2015 Jonny Heggheim <hegjon@gmail.com> - 1.8.2-0.1.git35ef764
- Inital packaging
