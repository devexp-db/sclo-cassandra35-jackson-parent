%{?scl:%scl_package jackson-parent}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jackson-parent
Version:	2.7
Release:	3.1%{?dist}
Summary:	Parent pom for all Jackson components
License:	ASL 2.0
URL:		https://github.com/FasterXML/jackson-parent
Source0:	https://github.com/FasterXML/%{pkg_name}/archive/%{pkg_name}-%{version}-1.tar.gz
# jackson-parent package don't include the license file
# reported @ https://github.com/FasterXML/jackson-parent/issues/1
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix}fasterxml-oss-parent
BuildRequires:	%{?scl_prefix}replacer
BuildRequires:	%{?scl_prefix_java_common}junit
%{?scl:Requires: %scl_runtime}

BuildArch:	noarch

%description
Project for parent pom for all Jackson components.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}-1

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build -j
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
* Mon Mar 06 2017 Tomas Repik <trepik@redhat.com> - 2.7-3.1
- scl conversion

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 22 2016 gil cattaneo <puntogil@libero.it> 2.7-1.1
- update to 2.7-1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 28 2015 gil cattaneo <puntogil@libero.it> 2.6.2-1
- update to 2.6.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 gil cattaneo <puntogil@libero.it> 2.5-1
- update to 2.5

* Wed Jul 02 2014 gil cattaneo <puntogil@libero.it> 2.4.1-1
- initial rpm
