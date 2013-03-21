%global luaver 5.1
%global luapkgdir %{_datadir}/lua/%{luaver}

# there's a circular (build) dependency with lua-ldoc
%global with_docs 1

Name:		lua-penlight
Version:	1.1.0
Release:	1%{?dist}
Summary:	Penlight Lua Libraries
License:	MIT
URL:		https://github.com/stevedonovan/Penlight
Source0:	https://github.com/stevedonovan/Penlight/archive/%{version}/Penlight-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	lua >= %{luaver}
BuildRequires:	lua-filesystem
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

# fix encoding
iconv -f iso-8859-1 -t utf-8 CHANGES.txt > CHANGES.txt.tmp
mv CHANGES.txt.tmp CHANGES.txt

# fix line-endings
sed -i 's/\r//' \
  README.txt LICENCE.txt CHANGES.txt \
  examples/*.lua

%if 0%{?with_docs}
# build docs
ldoc -c docs/config.ld .

# fix permissions
chmod u=rwX,go=rX -R docs/api
%endif # with_docs


%check
LUA_PATH="%{buildroot}%{luapkgdir}/?/init.lua;%{buildroot}%{luapkgdir}/?.lua;;" \
lua run.lua tests


%files
%doc README.txt CHANGES.txt LICENCE.txt
%{luapkgdir}/pl


%if 0%{?with_docs}
%files doc
%doc docs/api/*
%endif # with_docs


%files examples
%doc examples/*


%changelog
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
