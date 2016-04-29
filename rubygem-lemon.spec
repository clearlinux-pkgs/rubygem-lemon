#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-lemon
Version  : 0.9.1
Release  : 5
URL      : https://rubygems.org/downloads/lemon-0.9.1.gem
Source0  : https://rubygems.org/downloads/lemon-0.9.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: rubygem-lemon-bin
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# Lemon
[Homepage](http://rubyworks.github.com/lemon) |
[User Guide](http://wiki.github.com/rubyworks/lemon) |
[Development](http://github.com/rubyworks/lemon) |
[Issues](http://github.com/rubyworks/lemon/issues)

%package bin
Summary: bin components for the rubygem-lemon package.
Group: Binaries

%description bin
bin components for the rubygem-lemon package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n lemon-0.9.1
gem spec %{SOURCE0} -l --ruby > rubygem-lemon.gemspec

%build
gem build rubygem-lemon.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
lemon-0.9.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/lemon-0.9.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/.ruby
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/Config.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/SPECSHEET.md
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/bin/lemons
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon.yml
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/ae.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli/base.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli/coverage.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli/generate.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli/lemon.ascii
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli/obrother.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli/scaffold.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/cli/test.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/core_ext.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/core_ext/kernel.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/core_ext/module.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/analyzer.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/cover_unit.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/formats/abstract.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/formats/compact.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/formats/outline.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/formats/verbose.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/formats/yaml.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/snapshot.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/coverage/source_parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/ignore_callers.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_advice.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_case.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_class.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_class_method.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_method.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_module.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_proc.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_scope.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_setup.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/lib/lemon/test_world.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/spec/applique/ae.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/spec/applique/fs.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/spec/coverage/01_complete.md
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/spec/coverage/02_incomplete.md
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/spec/coverage/03_extensions.md
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/spec/coverage/applique/lemon.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/.test
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/case_error.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/case_fail.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/case_pass.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/case_pending.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/case_scope.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/case_singleton.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/case_untested.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/fixtures/calculator.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/fixtures/example-use.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/fixtures/example.rb
/usr/lib64/ruby/gems/2.3.0/gems/lemon-0.9.1/try/helpers/loadpath.rb
/usr/lib64/ruby/gems/2.3.0/specifications/lemon-0.9.1.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/lemons
