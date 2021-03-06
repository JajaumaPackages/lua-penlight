%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%global luapkgdir %{_datadir}/lua/%{luaver}

# there's a circular (build) dependency with lua-ldoc
%global with_docs 1

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		lua-penlight
Version:	1.5.4
Release:	3%{?dist}
Summary:	Penlight Lua Libraries
License:	MIT
URL:		https://github.com/stevedonovan/Penlight
Source0:	https://github.com/stevedonovan/Penlight/archive/%{version}/Penlight-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-filesystem
BuildRequires:	lua-markdown
%if 0%{?with_docs}
BuildRequires:	lua-ldoc
%endif # with_docs
Requires:	lua >= %{luaver}
Requires:	lua-filesystem

%global __requires_exclude_from %{_docdir}

%description
Penlight brings together a set of generally useful pure Lua modules,
focusing on input data handling (such as reading configuration
files), functional programming (such as map, reduce, placeholder
expressions,etc), and OS path management.  Much of the functionality
is inspired by the Python standard libraries.


%if 0%{?with_docs}
%package doc
Summary:	API docs for lua-penlight
Requires:	%{name} = %{version}-%{release}

%description doc
%{summary}
%endif # with_docs


%package examples
Summary:	Examples of lua-penlight usage
Requires:	%{name} = %{version}-%{release}

%description examples
%{summary}


%prep
%setup -q -n Penlight-%{version}


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{luapkgdir}
cp -av lua/pl %{buildroot}%{luapkgdir}

# fix scripts
chmod -x %{buildroot}%{luapkgdir}/pl/dir.lua

# build and install README etc.
mkdir -p %{buildroot}%{_pkgdocdir}
markdown.lua *.md
cp -av {README,CHANGES,CONTRIBUTING}.html %{buildroot}%{_pkgdocdir}

%if 0%{?with_docs}
# build and install docs
ldoc -c doc/config.ld .
cp -av doc/api %{buildroot}%{_pkgdocdir}
%endif # with_docs

# install examples
cp -av examples %{buildroot}%{_pkgdocdir}


%check
LUA_PATH="%{buildroot}%{luapkgdir}/?/init.lua;%{buildroot}%{luapkgdir}/?.lua;;" \
lua run.lua tests


%files
%dir %{_pkgdocdir}
%license LICENSE.html
%{_pkgdocdir}/README.html
%{_pkgdocdir}/CHANGES.html
%{_pkgdocdir}/CONTRIBUTING.html
%{luapkgdir}/pl


%if 0%{?with_docs}
%files doc
%{_pkgdocdir}/api
%endif # with_docs


%files examples
%{_pkgdocdir}/examples


%changelog
* Tue Aug 22 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.5.4-3
- Fixes for building with older lua on RHEL

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.4-1
- Update to 1.5.4.

* Wed May 17 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.2-2
- Re-enable docs.

* Tue May 16 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.2-1
- Update to 1.5.2.
- Minor spec file cleanups.

* Wed Apr  5 2017 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.0-1
- Update to 1.5.0.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.1-1
- Update to 1.4.1.
- Re-enable tests.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Mar 21 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.2-1
- Update to 1.3.2.
- Mark license with %%license.
- Re-enable tests.

* Sun Jan 18 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-5
- Own the package doc dir.
- Remove extra .md suffix from generated HTML files.

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.1-4
- build with docs

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.1-3
- rebuild for lua 5.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov  3 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-1
- Update to 1.3.1.
- Use a single package doc dir.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.0-2
- rebuild with docs

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1.1
- rebuild for lua 5.2, no docs

* Thu Mar 21 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.0-1
- Update to 1.1.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-3.a
- Add BR on lua-filesystem (needed when running the tests).
- Fix line-endings for the examples.

* Wed Jan  9 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-2.a
- Fix typos.
- Package examples as a separate subpackage.
- Run tests.

* Fri Jan  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-1.a
- New package.
