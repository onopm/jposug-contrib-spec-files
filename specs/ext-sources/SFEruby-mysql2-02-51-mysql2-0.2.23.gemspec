# -*- encoding: utf-8 -*-

Gem::Specification.new do |s|
  s.name = %q{mysql2}
  s.version = "0.2.23"

  s.required_rubygems_version = Gem::Requirement.new(">= 0") if s.respond_to? :required_rubygems_version=
  s.authors = ["Brian Lopez"]
  s.date = %q{2014-05-15}
  s.email = %q{seniorlopez@gmail.com}
  s.extensions = ["ext/mysql2/extconf.rb"]
  s.files = ["MIT-LICENSE", "README.md", "ext/mysql2/client.c", "ext/mysql2/client.h", "ext/mysql2/extconf.rb", "ext/mysql2/infile.c", "ext/mysql2/infile.h", "ext/mysql2/mysql2_ext.c", "ext/mysql2/mysql2_ext.h", "ext/mysql2/mysql_enc_name_to_ruby.h", "ext/mysql2/mysql_enc_to_ruby.h", "ext/mysql2/result.c", "ext/mysql2/result.h", "ext/mysql2/wait_for_single_fd.h", "lib/active_record/connection_adapters/mysql2_adapter.rb", "lib/arel/engines/sql/compilers/mysql2_compiler.rb", "lib/mysql2.rb", "lib/mysql2/client.rb", "lib/mysql2/console.rb", "lib/mysql2/em.rb", "lib/mysql2/error.rb", "lib/mysql2/result.rb", "lib/mysql2/version.rb", "support/mysql_enc_to_ruby.rb", "support/ruby_enc_to_mysql.rb", "examples/eventmachine.rb", "examples/threaded.rb", "spec/configuration.yml.example", "spec/em/em_spec.rb", "spec/my.cnf.example", "spec/mysql2/client_spec.rb", "spec/mysql2/error_spec.rb", "spec/mysql2/result_spec.rb", "spec/rcov.opts", "spec/spec_helper.rb", "spec/test_data"]
  s.homepage = %q{http://github.com/brianmario/mysql2}
  s.licenses = ["MIT"]
  s.rdoc_options = ["--charset=UTF-8"]
  s.require_paths = ["lib"]
  s.rubygems_version = %q{1.3.7}
  s.summary = %q{A simple, fast Mysql library for Ruby, binding to libmysql}
  s.test_files = ["examples/eventmachine.rb", "examples/threaded.rb", "spec/configuration.yml.example", "spec/em/em_spec.rb", "spec/my.cnf.example", "spec/mysql2/client_spec.rb", "spec/mysql2/error_spec.rb", "spec/mysql2/result_spec.rb", "spec/rcov.opts", "spec/spec_helper.rb", "spec/test_data"]

  if s.respond_to? :specification_version then
    current_version = Gem::Specification::CURRENT_SPECIFICATION_VERSION
    s.specification_version = 4

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_development_dependency(%q<eventmachine>, [">= 0"])
      s.add_development_dependency(%q<rake-compiler>, ["~> 0.8.1"])
      s.add_development_dependency(%q<rake>, ["~> 0.9.3"])
      s.add_development_dependency(%q<rspec>, ["~> 2.8.0"])
    else
      s.add_dependency(%q<eventmachine>, [">= 0"])
      s.add_dependency(%q<rake-compiler>, ["~> 0.8.1"])
      s.add_dependency(%q<rake>, ["~> 0.9.3"])
      s.add_dependency(%q<rspec>, ["~> 2.8.0"])
    end
  else
    s.add_dependency(%q<eventmachine>, [">= 0"])
    s.add_dependency(%q<rake-compiler>, ["~> 0.8.1"])
    s.add_dependency(%q<rake>, ["~> 0.9.3"])
    s.add_dependency(%q<rspec>, ["~> 2.8.0"])
  end
end
