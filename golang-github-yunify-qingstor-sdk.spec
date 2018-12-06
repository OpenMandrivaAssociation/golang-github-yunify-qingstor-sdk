# Run tests in check section
%bcond_without check

%global goipath         github.com/yunify/qingstor-sdk-go
Version:                2.2.15

%global common_description %{expand:
The official QingStor SDK for the Go programming language.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Official QingStor SDK for the Go programming language
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/pengsrc/go-shared/convert)
BuildRequires: golang(github.com/pengsrc/go-shared/log)
BuildRequires: golang(gopkg.in/yaml.v2)

%if %{with check}
BuildRequires:  golang(github.com/stretchr/testify)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup

rm -rf vendor


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md CHANGELOG.md AUTHORS docs


%changelog
* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.15-1
- Update to release 2.2.15

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.14-1
- Bump to 2.2.14

* Sun Apr 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.12-1
- First package for Fedora

